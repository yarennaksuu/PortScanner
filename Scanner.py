import socket
import argparse
import sys
import json
import ipaddress
import concurrent.futures
import ssl
import certifi
from datetime import datetime, timezone
from ftplib import FTP
from colorama import init, Fore, Style
from tqdm import tqdm

# Hacker-style cert decoding
from cryptography import x509
from cryptography.hazmat.backends import default_backend

# Initialize colors
init(autoreset=True)

# Global variable to store results
scan_results = []
# Global variable to store the original hostname for SNI
TARGET_HOSTNAME = None

def get_arguments():
    parser = argparse.ArgumentParser(description="PortScanner v2.5.1 - Final English")
    parser.add_argument("-t", "--target", dest="target", help="Target IP / CIDR / Domain", required=True)
    parser.add_argument("-o", "--output", dest="output", help="Output JSON file")
    options = parser.parse_args()
    return options

# --- PRO SSL ANALYSIS (SNI & UTC Fix) ---
def check_ssl_cert(ip, port):
    """Analyzes SSL certificate with proper SNI and UTC time handling."""
    try:
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        
        # SNI: Use domain name if available, otherwise IP
        server_name = TARGET_HOSTNAME if TARGET_HOSTNAME else ip

        with socket.create_connection((ip, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=server_name) as ssock:
                cert_bin = ssock.getpeercert(binary_form=True)
                
                if not cert_bin: return ""
                
                cert = x509.load_der_x509_certificate(cert_bin, default_backend())
                
                # Extract Common Name
                common_name = "Unknown"
                for attribute in cert.subject:
                    if attribute.oid == x509.NameOID.COMMON_NAME:
                        common_name = attribute.value
                        break
                
                # Extract Issuer
                issuer_org = "Unknown"
                for attribute in cert.issuer:
                    if attribute.oid == x509.NameOID.ORGANIZATION_NAME:
                        issuer_org = attribute.value
                        break
                
                # Calculate Expiry using UTC
                not_after = cert.not_valid_after_utc
                days_left = (not_after - datetime.now(timezone.utc)).days
                
                color = Fore.GREEN if days_left > 30 else Fore.RED
                return f" [SSL: {common_name} | Issuer: {issuer_org} | Expires: {color}{days_left} days{Fore.YELLOW}]"

    except Exception as e:
        return ""

# --- WAF DETECTION ---
def detect_waf(ip, port, is_https=False):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, port))
        
        if is_https:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            # SNI Fix for WAF
            server_name = TARGET_HOSTNAME if TARGET_HOSTNAME else ip
            s = context.wrap_socket(s, server_hostname=server_name)

        # Host header is crucial for WAFs
        host_header = TARGET_HOSTNAME if TARGET_HOSTNAME else ip
        payload = f"GET /?id=<script>alert('test')</script> HTTP/1.1\r\nHost: {host_header}\r\nUser-Agent: PortScanner\r\n\r\n"
        
        s.send(payload.encode())
        response = s.recv(1024).decode(errors='ignore')
        s.close()
        
        if "403 Forbidden" in response or "406 Not Acceptable" in response:
            return f" {Fore.MAGENTA}[!] WAF DETECTED (Blocked Attack){Style.RESET_ALL}"
        elif "Cloudflare" in response:
            return f" {Fore.MAGENTA}[!] WAF: Cloudflare Detected{Style.RESET_ALL}"
        elif "ModSecurity" in response:
            return f" {Fore.MAGENTA}[!] WAF: ModSecurity Detected{Style.RESET_ALL}"
        return ""
    except:
        return ""

# --- EXISTING CHECKS ---
def check_smtp_vrfy(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode(errors='ignore')
        s.send(b"VRFY root\r\n")
        response = s.recv(1024).decode(errors='ignore')
        s.close()
        if "250" in response or "252" in response:
            return True, "User Enumeration Allowed (VRFY root)"
        return False, ""
    except:
        return False, ""

def check_http_robots(ip, port, is_https=False):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        
        if is_https:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            server_name = TARGET_HOSTNAME if TARGET_HOSTNAME else ip
            s = context.wrap_socket(s, server_hostname=server_name)
        
        host_header = TARGET_HOSTNAME if TARGET_HOSTNAME else ip
        request = f"GET /robots.txt HTTP/1.1\r\nHost: {host_header}\r\nUser-Agent: PortScanner\r\n\r\n"
        s.send(request.encode())
        response = s.recv(1024).decode(errors='ignore')
        s.close()
        
        if "200 OK" in response:
             return True, "robots.txt found (Info Disclosure)"
        return False, ""
    except:
        return False, ""

def check_ftp_anonymous(ip, port):
    try:
        ftp = FTP()
        ftp.connect(ip, port, timeout=2)
        ftp.login('anonymous', 'anonymous')
        ftp.quit()
        return True, "Anonymous Login Allowed!"
    except:
        return False, ""

def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.5)
        s.connect((ip, port))
        try:
            banner = s.recv(1024).decode(errors='ignore').strip()
        except:
            banner = ""
        s.close()
        return banner
    except:
        return ""

# --- MAIN ORCHESTRATOR ---
def check_advanced_vulns(ip, port, banner, service):
    vuln_notes = ""
    
    if port == 21 or "ftp" in service:
        if "vsftpd 2.3.4" in banner:
             vuln_notes += f" {Fore.RED}[!] CRITICAL: vsftpd 2.3.4 Backdoor!{Style.RESET_ALL}"
        is_anon, msg = check_ftp_anonymous(ip, port)
        if is_anon:
            vuln_notes += f" {Fore.RED}[!] VULN: {msg}{Style.RESET_ALL}"
    
    elif port == 25 or "smtp" in service:
        is_vrfy, msg = check_smtp_vrfy(ip, port)
        if is_vrfy:
            vuln_notes += f" {Fore.RED}[!] VULN: {msg}{Style.RESET_ALL}"

    elif port in [80, 443, 8080] or "http" in service:
        is_https = (port == 443)
        
        waf_msg = detect_waf(ip, port, is_https=is_https)
        if waf_msg:
            vuln_notes += waf_msg
        
        if is_https:
            ssl_info = check_ssl_cert(ip, port)
            vuln_notes += f" {Fore.CYAN}{ssl_info}{Style.RESET_ALL}"
        
        has_robots, msg = check_http_robots(ip, port, is_https=is_https)
        if has_robots:
            vuln_notes += f" {Fore.YELLOW}[i] {msg}{Style.RESET_ALL}"
            
    elif port == 23 or "telnet" in service:
        vuln_notes += f" {Fore.RED}[!] INSECURE: Clear-text protocol!{Style.RESET_ALL}"

    return vuln_notes

def scan_target(ip, port):
    result_data = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((str(ip), port))
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            
            banner = grab_banner(str(ip), port)
            vuln = check_advanced_vulns(str(ip), port, banner, service)
            
            result_data = {
                "ip": str(ip),
                "port": port,
                "service": service,
                "banner": banner,
                "note": vuln.strip()
            }
        sock.close()
    except:
        pass
    
    return result_data

if __name__ == "__main__":
    options = get_arguments()
    target_input = options.target
    output_file = options.output
    
    try:
        # Detect if input is IP or Domain to store for SNI
        try:
            # Check if it is an IP
            ipaddress.ip_address(target_input)
            TARGET_HOSTNAME = None # It is an IP
        except ValueError:
            TARGET_HOSTNAME = target_input # It is a Domain

        target_list = list(ipaddress.IPv4Network(target_input, strict=False))
    except ValueError:
        try:
            resolved_ip = socket.gethostbyname(target_input)
            print(f"{Fore.YELLOW}[*] Domain resolved: {target_input} -> {resolved_ip}{Style.RESET_ALL}")
            target_list = [ipaddress.IPv4Address(resolved_ip)]
        except socket.gaierror:
            print(f"{Fore.RED}[!] Error: Invalid Target.{Style.RESET_ALL}")
            sys.exit()

    print("-" * 60)
    print(f"{Fore.CYAN}[*] Target: {target_input}")
    print(f"{Fore.CYAN}[*] Features: Port Scan, SSL SNI Analysis, WAF Detect, Vuln Check")
    print("-" * 60)
    
    total_tasks = len(target_list) * 1000
    
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = []
            
            for ip in target_list:
                for port in range(1, 1001):
                    futures.append(executor.submit(scan_target, ip, port))
            
            for future in tqdm(concurrent.futures.as_completed(futures), total=total_tasks, desc="Scanning", unit="port", ncols=80, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
                data = future.result()
                if data:
                    msg = f"{Fore.GREEN}[+] {data['ip']}:{data['port']:<5} ({data['service']}) OPEN {Fore.YELLOW}{data['banner']}{data['note']}"
                    tqdm.write(msg)
                    scan_results.append(data)
                    
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan cancelled.{Style.RESET_ALL}")
        sys.exit()

    print("-" * 60)
    print(f"{Fore.CYAN}[*] Scan Completed.")

    if output_file:
        try:
            with open(output_file, "w") as f:
                json.dump(scan_results, f, indent=4)
            print(f"{Fore.GREEN}[+] Report saved: {output_file}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error saving report.{Style.RESET_ALL}")