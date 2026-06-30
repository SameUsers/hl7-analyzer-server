# HL7 Analyzer Server

> **Open-source asynchronous Python HL7 v2.x server for veterinary laboratory analyzers.**
>
> Receive HL7 messages over TCP/MLLP, parse laboratory results, normalize analyzer data, and export structured JSON for integration with Veterinary Information Systems (VIS), Laboratory Information Systems (LIS), databases, or REST APIs.

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![License](https://img.shields.io/github/license/SameUsers/hl7-analyzer-server)
![GitHub Stars](https://img.shields.io/github/stars/SameUsers/hl7-analyzer-server)
![GitHub Issues](https://img.shields.io/github/issues/SameUsers/hl7-analyzer-server)

---

## Overview

HL7 Analyzer Server is an open-source Python framework for integrating **veterinary laboratory analyzers** using the **HL7 v2.x** protocol over **TCP/MLLP**.

Many veterinary analyzers provide proprietary Windows-only software that is difficult to integrate into modern systems. This project provides a clean, extensible, and production-ready alternative for receiving laboratory results directly from analyzers.

The architecture is protocol-oriented, asynchronous, and designed to support multiple analyzer models with minimal changes.

---

## Supported Analyzers

### Currently Supported

- ✅ Vet5160 Veterinary Hematology Analyzer
- ✅ Accent M320
- ✅ Seamaty SMT-120VP


### Planned Support

- Additional HL7-compatible veterinary analyzers

---

## Features

- Asynchronous TCP Server (AsyncIO)
- HL7 v2.x message processing
- MLLP framing support
- Automatic packet assembly
- HL7 parser
- Builder-based message processing
- JSON export
- Extensible architecture
- Dependency Injection
- Protocol-oriented interfaces
- Immutable DTO models
- Production-ready design
- Python 3.13+


## Architecture

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
│  │   Storage    │  │  (PostgreSQL)│  │  Endpoint    │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
│                                                                     │
│  ┌──────────────────────────────────────────────────────┐         │
│  │              Custom Storage Adapters                 │         │
│  │         (Plugins, Extensions, Third-party)           │         │
│  └──────────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow

```
Step 1: Analyzer sends HL7 message via TCP/MLLP
        ↓
Step 2: Server receives raw bytes
        ↓
Step 3: Detector extracts complete message using MLLP markers (0x0B ... 0x1C0D)
        ↓
Step 4: Parser converts HL7 string to structured segments
        ↓
Step 5: Builder normalizes data to device-specific format
        ↓
Step 6: Validation through Pydantic schema
        ↓
Step 7: Typed DTO (AnalyzeResult[T]) is created
        ↓
Step 8: Storage layer saves result to configured output
```

---

## Directory Structure

```
hl7-analyzer-server/
├── core/
│   ├── application/          # Application layer
│   │   ├── factories/        # Component factories
│   │   └── handlers/         # Request handlers
│   ├── contracts/            # Interfaces & abstract classes
│   ├── devices/              # Device-specific implementations
│   │   ├── accent_m320/      # Accent M320 biochemistry
│   │   ├── seamaty_smt/      # Seamaty SMT-120VP
│   │   └── vet_5160/         # Vet5160 hematology
│   ├── infrastructure/       # Infrastructure layer
│   │   ├── storage/          # Data storage
│   │   └── tcp/              # TCP server & buffer
│   ├── protocols/            # Protocol implementations
│   │   └── hl7/              # HL7 protocol
│   │       ├── framer.py     # Message framing
│   │       ├── parser.py     # HL7 parsing
│   │       └── segments/     # HL7 segment models
│   ├── schemas/              # Pydantic data schemas
│   └── shared/               # Shared utilities
├── Analyze/                  # Default JSON output directory
├── main.py                   # Entry point
└── pyproject.toml           # Project configuration
```

---

## Component Responsibilities

| Component | Responsibility | Input → Output |
|-----------|---------------|----------------|
| **TCP Server** | Accept connections, manage clients | Bytes → Bytes |
| **Session** | Manage client state | Connection → Session |
| **Packet Detector** | Extract complete messages using MLLP | Stream → Complete Message |
| **HL7 Parser** | Parse HL7 into structured data | String → HL7Message |
| **Builder** | Normalize analyzer-specific data | HL7Message → Device DTO |
| **Validator** | Validate data against schema | Device DTO → Validated DTO |
| **Storage** | Save results to configured output | Validated DTO → File/DB/API |

---

## Key Design Patterns

```
┌─────────────────────────────────────────────────────────────┐
│                    DESIGN PATTERNS                         │
├─────────────────────────────────────────────────────────────┤
│  Factory  → Creates handlers and components                 │
│  Builder  → Constructs analyzer results                    │
│  Singleton → Shared resources (parser, framer, storage)    │
│  Template → BaseHL7Builder with overridable methods        │
│  Strategy → Pluggable storage backends                     │
│  Observer → Event-driven processing                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

```
┌──────────────────┬──────────────────────────────────────────────┐
│   Component      │   Technology                                 │
├──────────────────┼──────────────────────────────────────────────┤
│ Language         │ Python 3.12+                                │
│ Runtime          │ AsyncIO                                     │
│ Validation       │ Pydantic v2                                 │
│ Logging          │ Loguru                                      │
│ Serialization    │ JSON                                        │
│ Package Manager  │ uv / pip                                    │
│ Testing          │ pytest (planned)                            │
│ Database         │ PostgreSQL (planned)                        │
│ API              │ FastAPI (planned)                           │
│ Containerization │ Docker (planned)                            │
│ Monitoring       │ Prometheus + Grafana (planned)              │
└──────────────────┴────────────────────────────────────────────
```

## Design Principles

The project follows modern software engineering practices:

- SOLID
- Clean Architecture
- Dependency Injection
- Builder Pattern
- Protocol-Oriented Programming
- AsyncIO-first Design
- Separation of Responsibilities
- Extensibility by Composition

---

## Installation

```bash
git clone https://github.com/SameUsers/hl7-analyzer-server.git

cd hl7-analyzer-server

pip install -r requirements.txt
```
---

## Running
```
python main.py
```
The server starts listening for incoming HL7 messages from compatible analyzers.

---

## Example Workflow
Analyzer
    │
    │ HL7 Message
    ▼
TCP Server
    │
    ▼
Packet Detector
    │
    ▼
Parser
    │
    ▼
Builder
    │
    ▼
AnalyzeResult DTO
    │
    ▼
JSON / Database / API

---

## Example HL7 Message
```
MSH|^~\&|Vet5160|LAB|VIS|SERVER|202606301200||ORU^R01|12345|P|2.3
PID|||10001||DOG^Lucky
OBR|1|||CBC
OBX|1|NM|WBC||7.42|10^9/L
OBX|2|NM|RBC||6.91|10^12/L
OBX|3|NM|HGB||15.1|g/dL
```
---

## Example JSON Output
```
{
  "device": "Vet5160",
  "patient": {
    "id": "10001",
    "name": "Lucky"
  },
  "results": [
    {
      "code": "1001",
      "name": "WBC",
      "value": 7.42
    },
    {
      "code": "1002",
      "name": "RBC",
      "value": 6.91
    },
    {
      "code": "1003",
      "name": "HGB",
      "value": 15.1
    }
  ]
}
```
---

## Why This Project?

There are many open-source HL7 libraries available, but very few focus specifically on veterinary laboratory analyzers.

This project aims to become a modern, open, and extensible platform for integrating veterinary diagnostic equipment with custom software.

Whether you're building:

- Veterinary Information Systems (VIS)
- Laboratory Information Systems (LIS)
- Clinic Management Software
- Cloud Laboratory Platforms
- Research Tools

this project provides a reliable foundation for receiving and processing HL7 messages.

---

## Roadmap
- Support additional analyzers
- HL7 ACK generation
- ASTM protocol support
- Automatic analyzer detection
- YAML configuration
- Database integrations
- REST API
- Docker image
- Prometheus metrics
- Grafana dashboards
- Plugin system
- Message validation
- Retry and buffering
- Multi-analyzer support
- Unit and integration tests

---

## Contributing

Contributions are welcome.

If you own another veterinary analyzer or would like to add support for additional devices, feel free to open an Issue or submit a Pull Request.

Bug reports, feature requests, and architecture discussions are always appreciated.

---

## License

This project is licensed under the MIT License.

---