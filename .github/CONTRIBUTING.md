# HL7 Analyzer Gateway

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/SameUsers/hl7-analyzer-server/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/SameUsers/hl7-analyzer-server)](https://github.com/SameUsers/hl7-analyzer-server/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/SameUsers/hl7-analyzer-server)](https://github.com/SameUsers/hl7-analyzer-server/issues)

Open-source asynchronous Python HL7 v2.x server for integration with veterinary laboratory analyzers.

The project is designed to receive laboratory results over TCP/MLLP, parse HL7 messages, normalize analyzer data, and export results in a structured JSON format. Although originally developed for the Vet5160 veterinary hematology analyzer, the architecture is protocol-oriented and can be extended to support additional analyzers with minimal effort.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Supported Analyzers](#supported-analyzers)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Project Goals](#project-goals)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 About the Project

**HL7 Analyzer Gateway** is an open-source asynchronous Python server that receives laboratory results from veterinary and medical analyzers over TCP/MLLP, parses HL7 v2.x messages, normalizes the data, and exports structured JSON results.

### Why This Project?

Most available HL7 libraries focus on human healthcare systems. This project specifically targets veterinary laboratory analyzers, making integration easier for:

- Veterinary clinics and hospitals
- Diagnostic laboratories
- Veterinary software developers
- Practice management system integrators

Many veterinary analyzers support HL7 communication but ship with proprietary Windows software that is difficult to integrate into modern web-based systems and laboratory information systems (LIS). This project aims to replace that with a modern, extensible, and well-documented Python solution.

### Author

I am a developer focused on open-source integration tools for veterinary diagnostics. I actively maintain this project and welcome contributions, feedback, and feature requests from the community.

---

## 🔌 Supported Analyzers

### Current Support

| Analyzer | Type | Status |
|----------|------|--------|
| **Vet5160** | Veterinary Hematology Analyzer (OAK) | ✅ Full support |

### Planned Support

| Analyzer | Type | Status |
|----------|------|--------|
| **Accent M320** | Biochemistry Analyzer (BAC) | 🔄 In progress |
| **Seamaty SMT-120VP** | Multi-channel Analyzer | 🔄 In progress |
| Other HL7-compatible analyzers | Various | 📝 Planned |

> **Need support for your analyzer?** [Open an issue](https://github.com/SameUsers/hl7-analyzer-server/issues) or contact me directly. I'll personally help you integrate it.

---

## ✨ Features

### Core Features

- ✅ **Asynchronous TCP server** built with AsyncIO
- ✅ **HL7 v2.x message processing**
- ✅ **MLLP framing support** (0x0B ... 0x1C0D)
- ✅ **Automatic message parsing**
- ✅ **Structured JSON export**
- ✅ **Protocol-oriented architecture**
- ✅ **Builder-based message parsing**
- ✅ **Easily extensible parser system**
- ✅ **Designed for long-running production services**
- ✅ **Python 3.12+**

### Technical Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.12+ |
| Runtime | AsyncIO |
| Validation | Pydantic v2 |
| Logging | Loguru |
| Serialization | JSON |
| Package Manager | uv / pip |

---

## 🏗️ Architecture

The server follows a clean architecture with clear separation of responsibilities.

### Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                        VETERINARY ANALYZER                        │
│                     (Vet5160, Accent M320, etc.)                  │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             │ HL7 v2.x over TCP/MLLP
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         TCP SERVER                                 │
│              (AsyncIO, port 8001, multiple clients)                │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           SESSION                                  │
│              (Client connection, state management)                 │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       PACKET DETECTOR                              │
│               (MLLP framing, message boundaries)                   │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         HL7 PARSER                                 │
│         (Segments: MSH, PID, OBR, OBX → Structured Data)          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           BUILDER                                  │
│         (Normalize data → Analyzer-specific DTO)                  │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      ANALYZE RESULT DTO                            │
│                   (Typed, validated Pydantic model)               │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         STORAGE LAYER                              │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │   JSON File  │  │  Database    │  │  REST API    │            │
│  │   Storage    │  │  (Planned)   │  │  (Planned)   │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────────────────────────┘
```

### Design Patterns

| Pattern | Usage |
|---------|-------|
| **Factory** | Creates handlers and components |
| **Builder** | Constructs analyzer results |
| **Singleton** | Shared resources (parser, framer, storage) |
| **Template** | BaseHL7Builder with overridable methods |
| **Strategy** | Pluggable storage backends |

---

## 📦 Installation

### Prerequisites

- Python 3.12+
- uv (recommended) or pip
- Git

### Method 1: Using uv (Recommended)

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repository
git clone https://github.com/SameUsers/hl7-analyzer-server.git
cd hl7-analyzer-server

# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

### Method 2: Using pip

```bash
# Clone repository
git clone https://github.com/SameUsers/hl7-analyzer-server.git
cd hl7-analyzer-server

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -e .
```

---

## 🚀 Usage

### Start the Server

```bash
python main.py
```

Expected output:
```
2026-06-30 14:45:23 | INFO | Server initialized on 0.0.0.0:8001
2026-06-30 14:45:23 | INFO | Server running on 0.0.0.0:8001
```

### Send Test Data

**Using Telnet:**
```bash
telnet localhost 8001
# Paste HL7 message with MLLP framing
\x0bMSH|^~\\&|LAB|CLINIC|...\x1c\x0d
```

**Using Python:**
```python
import socket

message = b"\x0b" + b"MSH|^~\\&|LAB|CLINIC|...|" + b"\x1c\x0d"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 8001))
    s.send(message)
```

### Check Results

```bash
ls Analyze/
# BAC/  OAK/  RED/  PINK/  YELLOW/  GREEN/  BROWN/

ls Analyze/OAK/2026-6-30/
# 2026-6-30-45-OAK.json
```

---

## 📊 Example Output

Results are saved in structured JSON format:

```json
{
  "analyzer_name": "5160Vet",
  "timestamp": "2026-06-30T14:45:23.123456",
  "result": {
    "analyze_type": "OAK",
    "WBC": 7.42,
    "RBC": 6.91,
    "HGB": 140.0,
    "HCT": 45.2,
    "PLT": 250.0,
    "LYM%": 25.4,
    "NEU#": 4.2,
    "MCV": 65.4,
    "MCH": 20.3,
    "MCHC": 310.0
  }
}
```

### Storage Structure

```
Analyze/
└── {analyzer_type}/
    └── {YYYY-MM-DD}/
        └── {YYYY-MM-DD-SS}-{analyzer_type}.json
```

---

## 🎯 Project Goals

The goal of this project is to provide an open-source integration platform for veterinary laboratory equipment. Many analyzers support HL7 but ship with proprietary Windows software. This project aims to replace that with a modern, extensible, and well-documented Python solution.

**My long-term vision**: A plugin-based, multi-analyzer integration platform that can serve as the backbone for veterinary laboratory information systems.

---

## 🗺️ Roadmap

### Short-term (v0.2.0)
- [ ] Add unit tests
- [ ] Environment configuration (.env)
- [ ] Health-check endpoint
- [ ] Docker image

### Medium-term (v0.3.0)
- [ ] Support for Accent M320
- [ ] Support for Seamaty SMT-120VP
- [ ] HL7 ACK generation
- [ ] Database storage (PostgreSQL)

### Long-term (v1.0.0)
- [ ] REST API
- [ ] Web dashboard
- [ ] Prometheus metrics
- [ ] Grafana monitoring
- [ ] Plugin system
- [ ] ASTM protocol support
- [ ] Multi-analyzer support
- [ ] Message validation
- [ ] Retry and buffering mechanisms

---

## 🤝 Contributing

Contributions are welcome in any form!

### How You Can Help

**For Developers:**
- Add support for your analyzer
- Improve the parser
- Write tests
- Review code
- Suggest architectural improvements

**For Veterinarians & Lab Technicians:**
- Test with real analyzers
- Provide feedback on output format
- Share your workflow needs
- Report issues

**For Everyone:**
- ⭐ Star the repository
- 🐛 Report bugs
- 📖 Improve documentation
- 💬 Join discussions
- 📢 Spread the word

**If you have an analyzer and want to integrate it**, I will personally help you get it working. Open an issue or contact me directly.

See [CONTRIBUTING.md](https://github.com/SameUsers/hl7-analyzer-server/blob/main/.github/CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](https://github.com/SameUsers/hl7-analyzer-server/blob/main/LICENSE) file for details.

---

## 📞 Contact

**Author**: SameUsers  
**GitHub**: [SameUsers/hl7-analyzer-server](https://github.com/SameUsers/hl7-analyzer-server)  
 

---

## 🙏 Acknowledgments

- [Pydantic](https://github.com/pydantic/pydantic) — Data validation
- [Loguru](https://github.com/Delgan/loguru) — Logging
- [uv](https://github.com/astral-sh/uv) — Package management

---

## ⭐ Support the Project

If you find this project useful:

1. ⭐ **Star** the repository on GitHub
2. 🔄 **Share** it with colleagues
3. 💬 **Start** a discussion
4. 🐛 **Report** bugs
5. 🔧 **Contribute** code

Let's build the open-source infrastructure for veterinary diagnostics together.

---
