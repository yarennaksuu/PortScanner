import socket
import argparse
import sys
from datetime import datetime
import concurrent.futures
from colorama import init, Fore

# Initialize colorama
init()

def get_arguments():
    parser = argparse.ArgumentParser(description="Advanced Port Scanner with Banner Grabbing")
    parser.add_argument("-t", "--target", dest="target", help="Target IP Address", required=True)
    options = parser.parse_args()
    return options

def grab_banner(ip, port):
    try:
        # Create a new socket for banner grabbing
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        
        # Receive data (max 1024 bytes)
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return ""

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            # Get Service Name
            try:
                service_name = socket.getservbyport(port)
            except:
                service_name = "Unknown"
            
            # Get Banner (Version Info)
            banner = grab_banner(ip, port)
            
            # Print Output
            if banner:
                print(f"{Fore.GREEN}[+] Port {port:<5} ({service_name}) OPEN : {Fore.YELLOW}{banner}{Fore.RESET}")
            else:
                print(f"{Fore.GREEN}[+] Port {port:<5} ({service_name}) is OPEN{Fore.RESET}")
            
        sock.close()
    except Exception:
        pass

if __name__ == "__main__":
    try:
        user_input = get_arguments()
        target_ip = user_input.target
    except:
        print(f"{Fore.RED}Please specify a target.{Fore.RESET}")
        sys.exit()
    
    print("-" * 60)
    print(f"{Fore.CYAN}[*] Scanning Target: {target_ip}{Fore.RESET}")
    print(f"{Fore.CYAN}[*] Scanning ports 1-1000 with 100 threads...{Fore.RESET}")
    print(f"{Fore.CYAN}[*] Start Time: {str(datetime.now())}{Fore.RESET}")
    print("-" * 60)

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1, 1001):
                executor.submit(scan_port, target_ip, port)
            
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Exiting...{Fore.RESET}")
        sys.exit()
    except socket.gaierror:
        print(f"\n{Fore.RED}[!] Hostname could not be resolved.{Fore.RESET}")
        sys.exit()
    except socket.error:
        print(f"\n{Fore.RED}[!] Could not connect to server.{Fore.RESET}")
        sys.exit()

    print("-" * 60)
    print(f"{Fore.CYAN}[*] Scan Completed: {str(datetime.now())}{Fore.RESET}")