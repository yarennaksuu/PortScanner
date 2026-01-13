import socket
import argparse
import sys
from datetime import datetime

def get_arguments():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("-t", "--target", dest="target", help="Target IP Address", required=True)
    options = parser.parse_args()
    return options

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
            
        sock.close()
    except Exception:
        pass

if __name__ == "__main__":
    try:
        user_input = get_arguments()
        target_ip = user_input.target
    except:
        print("Please specify a target. Example: python Scanner.py -t 8.8.8.8")
        sys.exit()
    
    print("-" * 50)
    print(f"[*] Scanning Target: {target_ip}")
    print(f"[*] Start Time: {str(datetime.now())}")
    print("-" * 50)

    try:
        # Scanning ports 1 to 1000
        for port in range(1, 1001): 
            scan_port(target_ip, port)
            
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\n[!] Could not connect to server.")
        sys.exit()