# ⚡ Advanced Port Scanner v2.0

<div align="center">

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**A blazing-fast, feature-rich network port scanner with a beautiful terminal UI**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

### ⚡ **Performance**
- **100x Faster** than traditional scanners with multi-threading
- Scan **100+ ports per second** with default settings
- Configurable worker threads (10-500+)
- Optimized connection handling with thread pooling

### 🎨 **Beautiful UI**
- Colorized terminal output for better readability
- Professional ASCII banner
- Real-time progress tracking
- Clean, intuitive result presentation
- Comprehensive scan statistics

### 🔍 **Smart Scanning**
- **Service Detection** - Automatically identifies 40+ common services
- **Flexible Port Selection**:
  - Port ranges: `1-1000`
  - Specific ports: `22,80,443`
  - Combined: `1-100,443,8080-8090`
- **Preset Scan Modes**:
  - Common ports (1-1024) - Default
  - Full scan (all 65535 ports)
  - Top N most common ports

### 💾 **Export Capabilities**
- **Multiple formats**: JSON, CSV, TXT
- Timestamped results
- Detailed scan metadata
- Easy integration with other tools

### 🎛️ **Customization**
- Adjustable connection timeout
- Configurable thread count
- Quiet mode for scripting
- Banner toggle
- Flexible output options

---

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies! Uses only Python standard library

---

## 🚀 Installation

### Option 1: Clone the Repository
```bash
git clone https://github.com/yourusername/advanced-port-scanner.git
cd advanced-port-scanner
chmod +x port_scanner.py
```

### Option 2: Direct Download
```bash
wget https://raw.githubusercontent.com/yourusername/advanced-port-scanner/main/port_scanner.py
chmod +x port_scanner.py
```

---

## 💻 Usage

### Basic Syntax
```bash
python port_scanner.py -t <target> [options]
```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-t, --target` | Target IP address or hostname (required) | - |
| `-p, --ports` | Port range to scan | 1-1024 |
| `--full` | Scan all 65535 ports | False |
| `--top N` | Scan top N common ports | - |
| `-w, --workers` | Number of concurrent threads | 100 |
| `-T, --timeout` | Connection timeout in seconds | 1.0 |
| `-o, --output` | Export results to file | - |
| `-f, --format` | Output format (json/csv/txt) | json |
| `--no-banner` | Hide ASCII banner | False |
| `--quiet` | Minimal output (for scripting) | False |

### Getting Help
```bash
python port_scanner.py -h
```

---

## 📚 Examples

### Basic Scans

**Scan common ports (1-1024)**
```bash
python port_scanner.py -t 192.168.1.1
```

**Scan specific ports**
```bash
python port_scanner.py -t example.com -p 80,443,8080
```

**Scan a port range**
```bash
python port_scanner.py -t 192.168.1.1 -p 1-1000
```

**Scan top 50 most common ports**
```bash
python port_scanner.py -t example.com --top 50
```

### Advanced Scans

**Full port scan (all 65535 ports)**
```bash
python port_scanner.py -t 192.168.1.1 --full
```

**Fast scan with 200 threads**
```bash
python port_scanner.py -t example.com -p 1-10000 -w 200
```

**Custom timeout for slow networks**
```bash
python port_scanner.py -t example.com -T 2.0
```

**Combined port specification**
```bash
python port_scanner.py -t 192.168.1.1 -p 1-100,443,8080-8090,3306
```

### Export Results

**Export to JSON**
```bash
python port_scanner.py -t 192.168.1.1 -o results.json
```

**Export to CSV**
```bash
python port_scanner.py -t example.com -o results.csv -f csv
```

**Export to TXT**
```bash
python port_scanner.py -t 192.168.1.1 -o results.txt -f txt
```

### Scripting & Automation

**Quiet mode with JSON export**
```bash
python port_scanner.py -t 192.168.1.1 --quiet -o scan_$(date +%Y%m%d).json
```

**Scan multiple targets**
```bash
for ip in 192.168.1.{1..10}; do
  python port_scanner.py -t $ip --quiet -o "scan_$ip.json"
done
```

**Cron job example**
```bash
# Daily scan at 2 AM
0 2 * * * /usr/bin/python3 /path/to/port_scanner.py -t myserver.com --quiet -o /var/log/port_scan_$(date +\%Y\%m\%d).json
```

---

## 📊 Sample Output

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║              ⚡ ADVANCED PORT SCANNER v2.0 ⚡              ║
║                                                               ║
║          Fast • Powerful • Feature-Rich                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

✓ Target resolved: example.com → 93.184.216.34

⚡ Scanning 1024 ports with 100 threads...

PORT     STATUS       SERVICE            
──────────────────────────────────────────────────
22       OPEN         SSH                
80       OPEN         HTTP               
443      OPEN         HTTPS              
3306     OPEN         MySQL              
8080     OPEN         HTTP-Proxy         

══════════════════════════════════════════════════
📊 SCAN SUMMARY
══════════════════════════════════════════════════
Target:          example.com
Duration:        10.34 seconds
Ports Scanned:   1024
Open Ports:      5
Closed Ports:    1019
Scan Speed:      99 ports/sec
══════════════════════════════════════════════════

✓ Results exported to: results.json
```

---

## 🎯 Supported Services

The scanner automatically detects these common services:

| Port | Service | Port | Service | Port | Service |
|------|---------|------|---------|------|---------|
| 21 | FTP | 80 | HTTP | 443 | HTTPS |
| 22 | SSH | 110 | POP3 | 3306 | MySQL |
| 23 | Telnet | 143 | IMAP | 3389 | RDP |
| 25 | SMTP | 445 | SMB | 5432 | PostgreSQL |
| 53 | DNS | 993 | IMAPS | 6379 | Redis |

And 25+ more! See the code for the complete list.

---

## ⚙️ Performance Tips

### Optimize Scan Speed

**For local networks (fast)**
```bash
python port_scanner.py -t 192.168.1.1 -w 200 -T 0.5
```

**For remote hosts (stable)**
```bash
python port_scanner.py -t example.com -w 100 -T 1.0
```

**For slow/unreliable networks**
```bash
python port_scanner.py -t example.com -w 50 -T 3.0
```

### Benchmarks

| Scan Type | Ports | Time | Speed |
|-----------|-------|------|-------|
| Common Ports | 1,024 | ~10 sec | 100+ ports/sec |
| Extended | 10,000 | ~1.5 min | 110+ ports/sec |
| Full Scan | 65,535 | ~11 min | 100+ ports/sec |

*Results may vary based on network conditions and target responsiveness*

---

## 📖 Export Format Examples

### JSON Output
```json
{
  "target": "example.com",
  "scan_time": "2025-10-01T10:30:45.123456",
  "duration": 10.34,
  "open_ports": [
    {"port": 22, "service": "SSH"},
    {"port": 80, "service": "HTTP"},
    {"port": 443, "service": "HTTPS"}
  ],
  "total_scanned": 1024
}
```

### CSV Output
```csv
Port,Service,Status
22,SSH,OPEN
80,HTTP,OPEN
443,HTTPS,OPEN
```

### TXT Output
```
Port Scan Results for example.com
Scan Date: 2025-10-01 10:30:45.123456
Duration: 10.34 seconds

OPEN PORTS:
----------------------------------------
Port 22: SSH
Port 80: HTTP
Port 443: HTTPS
```

---

## ⚠️ Legal Disclaimer

**IMPORTANT:** This tool is provided for **educational purposes and authorized security testing only**.

- ✅ **DO**: Use on your own systems or with explicit written permission
- ✅ **DO**: Use for legitimate security assessments and network diagnostics
- ✅ **DO**: Comply with all applicable laws and regulations
- ❌ **DON'T**: Scan systems without authorization
- ❌ **DON'T**: Use for malicious purposes
- ❌ **DON'T**: Violate any terms of service or laws

**Unauthorized port scanning may be illegal in your jurisdiction.** Users are solely responsible for ensuring their use complies with all applicable laws. The authors assume no liability for misuse of this tool.

---

## 🤝 Contributing

We love contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report bugs
- How to suggest features
- Pull request guidelines
- Code style standards
- Development workflow

### Quick Start for Contributors
```bash
# Fork and clone the repo
git clone https://github.com/yourusername/advanced-port-scanner.git
cd advanced-port-scanner

# Create a feature branch
git checkout -b feature/amazing-feature

# Make your changes and commit
git commit -m "Add: amazing new feature"

# Push and create a pull request
git push origin feature/amazing-feature
```

---

## 🗺️ Roadmap

### Completed ✅
- [x] Multi-threading for blazing-fast scans
- [x] Service detection and identification
- [x] Export to multiple formats (JSON, CSV, TXT)
- [x] Beautiful colorized terminal UI
- [x] Real-time progress tracking
- [x] Comprehensive CLI options

### In Progress 🚧
- [ ] UDP port scanning support
- [ ] Banner grabbing for detailed service info
- [ ] OS detection capabilities
- [ ] Stealth scan modes

### Planned 📋
- [ ] GUI interface (Tkinter/PyQt)
- [ ] IPv6 support
- [ ] Vulnerability detection
- [ ] Network mapping visualization
- [ ] Custom service definitions
- [ ] Scan profiles and templates
- [ ] API/library mode
- [ ] Docker image

---

## 🏆 Credits & Acknowledgments

### Author
Created with ❤️ by [Your Name](https://github.com/yourusername)

### Inspiration
- Nmap - The legendary network scanner
- Masscan - For speed optimization ideas
- Python Socket Programming community

### Contributors
Thanks to all the amazing people who have contributed to this project!

<!-- Add contributor list here -->

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/advanced-port-scanner/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/advanced-port-scanner/discussions)
- **Email**: your.email@example.com
- **Twitter**: [@yourhandle](https://twitter.com/yourhandle)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## ⭐ Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 💡 Suggesting new features
- 🤝 Contributing code
- 📢 Sharing with others

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/advanced-port-scanner?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/advanced-port-scanner?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/advanced-port-scanner)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/advanced-port-scanner)

---

<div align="center">

**Made with 💻 and ☕**

[⬆ Back to Top](#-advanced-port-scanner-v20)

</div>