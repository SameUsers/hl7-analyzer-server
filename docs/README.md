# HL7 Analyzer Gateway Documentation

Welcome to the documentation for HL7 Analyzer Gateway — an open-source asynchronous Python HL7 v2.x server for integrating veterinary laboratory analyzers.

---

## 📚 Documentation Index

### Getting Started
- [Installation Guide](installation.md)
- [Quick Start](quickstart.md)
- [Configuration](configuration.md)

### User Guide
- [Running the Server](running.md)
- [Adding Analyzers](adding-analyzers.md)
- [Output Format](output-format.md)
- [Troubleshooting](troubleshooting.md)

### Developer Guide
- [Architecture Overview](architecture.md)
- [Adding New Analyzers](adding-analyzers.md)
- [HL7 Protocol](hl7-protocol.md)
- [API Reference](api-reference.md)

### Community
- [Contributing Guide](../.github/CONTRIBUTING.md)
- [Code of Conduct](../.github/CODE_OF_CONDUCT.md)
- [FAQ](faq.md)

---

## 🔗 Quick Links

- [GitHub Repository](https://github.com/SameUsers/hl7-analyzer-server)
- [Issue Tracker](https://github.com/SameUsers/hl7-analyzer-server/issues)
- [Discussions](https://github.com/SameUsers/hl7-analyzer-server/discussions)
- [Releases](https://github.com/SameUsers/hl7-analyzer-server/releases)

---

## 📖 About

HL7 Analyzer Gateway is a production-ready TCP server that:
- Receives HL7 messages from analyzers via TCP/MLLP
- Parses and validates the data
- Normalizes it to structured formats
- Exports results as JSON

**Current Support:**
- Vet5160 Veterinary Hematology Analyzer

**Planned:**
- Accent M320
- Seamaty SMT-120VP
- And more...

---

## 🚀 Quick Start

```bash
git clone https://github.com/SameUsers/hl7-analyzer-server.git
cd hl7-analyzer-server
uv sync
python main.py