import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """Scan a single port on the target host."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 second timeout
        
        # Attempt to connect
        result = sock.connect_ex((target, port))
        sock.close()
        
        return result == 0  # Returns True if port is open
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

def main():
    # Get target from user
    target = input("Enter target IP or hostname: ")
    
    # Resolve hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    
    print(f"\nScanning target: {target} ({target_ip})")
    print(f"Time started: {datetime.now()}\n")
    print("-" * 50)
    
    # Scan common ports (you can modify this range)
    start_port = 1
    end_port = 1024
    
    open_ports = []
    
    try:
        for port in range(start_port, end_port + 1):
            if scan_port(target_ip, port):
                print(f"Port {port}: OPEN")
                open_ports.append(port)
        
        print("-" * 50)
        print(f"\nScan completed at {datetime.now()}")
        print(f"Found {len(open_ports)} open port(s)")
        
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user.")
        sys.exit()

if __name__ == "__main__":
    main()
