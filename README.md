# Simple Port Scanner

A lightweight, easy-to-use port scanner written in Python for network diagnostics and security testing.

## Features

- 🚀 Fast and efficient TCP port scanning
- 🎯 Scan specific hosts by IP or hostname
- ⏱️ Configurable timeout settings
- 📊 Clear scan results and progress tracking
- 🔧 Easy to customize port ranges
- 💻 Simple command-line interface

## Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses standard library only)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simple-port-scanner.git
cd simple-port-scanner
```

2. Make the script executable (optional):
```bash
chmod +x port_scanner.py
```

## Usage

Run the scanner:
```bash
python port_scanner.py
```

When prompted, enter the target IP address or hostname:
```
Enter target IP or hostname: 192.168.1.1
```

The scanner will display open ports as it finds them:
```
Scanning target: 192.168.1.1 (192.168.1.1)
Time started: 2025-10-01 10:30:45.123456

--------------------------------------------------
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
--------------------------------------------------

Scan completed at 2025-10-01 10:31:52.789012
Found 3 open port(s)
```

## Customization

### Changing Port Range

Edit the `main()` function to modify the port range:
```python
start_port = 1      # First port to scan
end_port = 1024     # Last port to scan
```

### Adjusting Timeout

Modify the timeout in the `scan_port()` function:
```python
sock.settimeout(1)  # Change to desired timeout in seconds
```

### Scanning Specific Ports

Replace the range loop with a list of specific ports:
```python
ports_to_scan = [21, 22, 80, 443, 3306, 8080]
for port in ports_to_scan:
    if scan_port(target_ip, port):
        print(f"Port {port}: OPEN")
```

## Legal Disclaimer

⚠️ **IMPORTANT:** This tool is provided for educational purposes and authorized security testing only.

- Only scan networks and systems you own or have explicit written permission to test
- Unauthorized port scanning may be illegal in your jurisdiction
- Users are responsible for complying with all applicable laws and regulations
- The authors assume no liability for misuse of this tool

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## Roadmap

- [ ] Multi-threading for faster scans
- [ ] UDP port scanning support
- [ ] Service detection and banner grabbing
- [ ] Output to file (JSON, CSV, TXT)
- [ ] GUI interface
- [ ] Progress bar for long scans
- [ ] IPv6 support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Your Name - [@yourhandle](https://twitter.com/yourhandle)

## Acknowledgments

- Built with Python's standard `socket` library
- Inspired by tools like Nmap and other network utilities
- Thanks to all contributors who help improve this project

## Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new features
- 🤝 Contributing code improvements

## Contact

- GitHub Issues: [Project Issues](https://github.com/yourusername/simple-port-scanner/issues)
- Email: your.email@example.com

---

**Remember:** Always use this tool responsibly and ethically.
