#!/usr/bin/env python3
"""
Advanced Port Scanner with Beautiful UI
A feature-rich network scanning tool with multi-threading, service detection, and progress tracking.
"""

import socket
import sys
import argparse
import json
import csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Tuple
import time

# ANSI color codes for beautiful terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Common port services mapping
COMMON_PORTS = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP", 68: "DHCP", 69: "TFTP", 80: "HTTP",
    110: "POP3", 123: "NTP", 135: "MS-RPC", 137: "NetBIOS", 138: "NetBIOS",
    139: "NetBIOS", 143: "IMAP", 161: "SNMP", 162: "SNMP-TRAP", 389: "LDAP",
    443: "HTTPS", 445: "SMB", 465: "SMTPS", 514: "Syslog", 587: "SMTP",
    636: "LDAPS", 993: "IMAPS", 995: "POP3S", 1433: "MSSQL", 1521: "Oracle",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
    8080: "HTTP-Proxy", 8443: "HTTPS-Alt", 27017: "MongoDB", 9200: "Elasticsearch"
}

class PortScanner:
    def __init__(self, target: str, timeout: float = 1.0, max_workers: int = 100):
        self.target = target
        self.timeout = timeout
        self.max_workers = max_workers
        self.open_ports = []
        self.closed_ports = []
        self.start_time = None
        self.end_time = None
        
    def print_banner(self):
        """Display beautiful ASCII banner"""
        banner = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              {Colors.BOLD}⚡ ADVANCED PORT SCANNER v2.0 ⚡{Colors.ENDC}{Colors.CYAN}                 ║
║                                                               ║
║          {Colors.GREEN}Fast • Powerful • Feature-Rich{Colors.ENDC}{Colors.CYAN}                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.ENDC}
"""
        print(banner)
    
    def resolve_target(self) -> str:
        """Resolve hostname to IP address"""
        try:
            ip = socket.gethostbyname(self.target)
            print(f"{Colors.GREEN}✓{Colors.ENDC} Target resolved: {Colors.BOLD}{self.target}{Colors.ENDC} → {Colors.CYAN}{ip}{Colors.ENDC}")
            return ip
        except socket.gaierror:
            print(f"{Colors.RED}✗ Error:{Colors.ENDC} Could not resolve hostname: {self.target}")
            sys.exit(1)
    
    def get_service_name(self, port: int) -> str:
        """Get service name for a port"""
        return COMMON_PORTS.get(port, "Unknown")
    
    def scan_port(self, ip: str, port: int) -> Tuple[int, bool, str]:
        """Scan a single port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            
            if result == 0:
                service = self.get_service_name(port)
                return port, True, service
            return port, False, ""
        except Exception:
            return port, False, ""
    
    def scan_ports(self, ip: str, ports: List[int], show_progress: bool = True):
        """Scan multiple ports with multi-threading"""
        print(f"\n{Colors.YELLOW}⚡ Scanning {len(ports)} ports with {self.max_workers} threads...{Colors.ENDC}\n")
        print(f"{Colors.BLUE}{'PORT':<8} {'STATUS':<12} {'SERVICE':<20}{Colors.ENDC}")
        print("─" * 50)
        
        self.start_time = time.time()
        scanned = 0
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_port = {executor.submit(self.scan_port, ip, port): port for port in ports}
            
            for future in as_completed(future_to_port):
                port, is_open, service = future.result()
                scanned += 1
                
                if is_open:
                    self.open_ports.append({'port': port, 'service': service})
                    print(f"{Colors.GREEN}{port:<8} {'OPEN':<12} {service:<20}{Colors.ENDC}")
                else:
                    self.closed_ports.append(port)
                
                if show_progress and scanned % 100 == 0:
                    progress = (scanned / len(ports)) * 100
                    print(f"{Colors.CYAN}Progress: {scanned}/{len(ports)} ({progress:.1f}%){Colors.ENDC}", end='\r')
        
        self.end_time = time.time()
        
        if show_progress:
            print(" " * 50, end='\r')  # Clear progress line
    
    def print_summary(self):
        """Print scan summary"""
        duration = self.end_time - self.start_time
        
        print("\n" + "═" * 50)
        print(f"{Colors.BOLD}{Colors.CYAN}📊 SCAN SUMMARY{Colors.ENDC}")
        print("═" * 50)
        print(f"Target:          {Colors.BOLD}{self.target}{Colors.ENDC}")
        print(f"Duration:        {Colors.YELLOW}{duration:.2f} seconds{Colors.ENDC}")
        print(f"Ports Scanned:   {len(self.open_ports) + len(self.closed_ports)}")
        print(f"Open Ports:      {Colors.GREEN}{len(self.open_ports)}{Colors.ENDC}")
        print(f"Closed Ports:    {Colors.RED}{len(self.closed_ports)}{Colors.ENDC}")
        print(f"Scan Speed:      {Colors.CYAN}{(len(self.open_ports) + len(self.closed_ports)) / duration:.0f} ports/sec{Colors.ENDC}")
        print("═" * 50 + "\n")
    
    def export_results(self, format: str, filename: str):
        """Export results to file"""
        try:
            if format == 'json':
                data = {
                    'target': self.target,
                    'scan_time': datetime.now().isoformat(),
                    'duration': self.end_time - self.start_time,
                    'open_ports': self.open_ports,
                    'total_scanned': len(self.open_ports) + len(self.closed_ports)
                }
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
            
            elif format == 'csv':
                with open(filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Port', 'Service', 'Status'])
                    for item in self.open_ports:
                        writer.writerow([item['port'], item['service'], 'OPEN'])
            
            elif format == 'txt':
                with open(filename, 'w') as f:
                    f.write(f"Port Scan Results for {self.target}\n")
                    f.write(f"Scan Date: {datetime.now()}\n")
                    f.write(f"Duration: {self.end_time - self.start_time:.2f} seconds\n\n")
                    f.write("OPEN PORTS:\n")
                    f.write("-" * 40 + "\n")
                    for item in self.open_ports:
                        f.write(f"Port {item['port']}: {item['service']}\n")
            
            print(f"{Colors.GREEN}✓{Colors.ENDC} Results exported to: {Colors.BOLD}{filename}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.RED}✗ Export failed:{Colors.ENDC} {str(e)}")

def parse_port_range(port_str: str) -> List[int]:
    """Parse port range string (e.g., '1-100,443,8080')"""
    ports = []
    for part in port_str.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.extend(range(start, end + 1))
        else:
            ports.append(int(part))
    return sorted(set(ports))

def main():
    parser = argparse.ArgumentParser(
        description='Advanced Port Scanner - Fast, powerful network scanning tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s -t 192.168.1.1                    # Scan common ports
  %(prog)s -t example.com -p 1-1000          # Scan ports 1-1000
  %(prog)s -t 192.168.1.1 -p 80,443,8080     # Scan specific ports
  %(prog)s -t example.com --full             # Scan all 65535 ports
  %(prog)s -t 192.168.1.1 -o results.json    # Export to JSON
        """
    )
    
    parser.add_argument('-t', '--target', required=True, help='Target IP or hostname')
    parser.add_argument('-p', '--ports', default='1-1024', help='Port range (default: 1-1024)')
    parser.add_argument('--full', action='store_true', help='Scan all 65535 ports')
    parser.add_argument('--top', type=int, metavar='N', help='Scan top N common ports')
    parser.add_argument('-w', '--workers', type=int, default=100, help='Number of worker threads (default: 100)')
    parser.add_argument('-T', '--timeout', type=float, default=1.0, help='Connection timeout in seconds (default: 1.0)')
    parser.add_argument('-o', '--output', help='Export results to file')
    parser.add_argument('-f', '--format', choices=['json', 'csv', 'txt'], default='json', help='Output format (default: json)')
    parser.add_argument('--no-banner', action='store_true', help='Hide banner')
    parser.add_argument('--quiet', action='store_true', help='Minimal output')
    
    args = parser.parse_args()
    
    try:
        scanner = PortScanner(args.target, timeout=args.timeout, max_workers=args.workers)
        
        if not args.no_banner and not args.quiet:
            scanner.print_banner()
        
        ip = scanner.resolve_target()
        
        # Determine ports to scan
        if args.full:
            ports = list(range(1, 65536))
        elif args.top:
            top_ports = sorted(COMMON_PORTS.keys())[:args.top]
            ports = top_ports
        else:
            ports = parse_port_range(args.ports)
        
        # Perform scan
        scanner.scan_ports(ip, ports, show_progress=not args.quiet)
        
        # Print summary
        if not args.quiet:
            scanner.print_summary()
        
        # Export results
        if args.output:
            scanner.export_results(args.format, args.output)
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠ Scan interrupted by user{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}✗ Error:{Colors.ENDC} {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()