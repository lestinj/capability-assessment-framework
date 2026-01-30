# Capability Assessment Framework (CAF)

AI-driven enterprise architecture capability assessment platform that automates what traditionally takes consulting firms 24+ weeks and $500K-$2M.

## Overview

The Capability Assessment Framework uses multi-agent AI to analyze enterprise architecture documentation, conduct capability assessments, identify gaps, and generate transformation roadmaps — reducing assessment time from **24 weeks to ~2 weeks** while maintaining assessment quality.

## Project Status

🚧 **Active Development** — Building proof of concept for VIPC grant application

## Key Features (Planned)

- **Automated Document Analysis** — NLP extraction of capabilities, technologies, and dependencies
- **Multi-Agent Assessment Crews** — Specialized agents for technical debt, business value, and risk assessment
- **RAG Integration** — Retrieval-augmented generation for institutional knowledge
- **MCP Tools** — Model Context Protocol for enterprise system integration (ServiceNow, CMDB, etc.)

## Tech Stack

| Component | Technology |
|-----------|------------|
| Agent Orchestration | LangGraph, CrewAI |
| LLM | Llama 3.1 70B (Ollama dev / vLLM prod) |
| Embeddings | BGE-large-en-v1.5 |
| Vector Database | Qdrant |
| Reranker | BGE-reranker-v2-m3 |

## Project Structure

```
capability-assessment-framework/
├── README.md                    # This file
├── CLAUDE.md                    # Context for Claude AI integration
├── requirements.txt             # Python dependencies
├── config/
│   └── settings.yaml            # Configuration
├── docs/
│   ├── architecture.md          # System design
│   ├── retrospectives/          # POC case studies
│   └── vipc-application/        # Grant materials
├── src/
│   ├── agents/                  # Assessment agents
│   │   ├── intake_agent.py      # Document intake & classification
│   │   ├── discovery_agent.py   # Capability discovery
│   │   ├── assessment_agent.py  # Gap analysis
│   │   └── reporting_agent.py   # Report generation
│   ├── rag/                     # RAG pipeline
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   └── retriever.py
│   ├── orchestration/           # Workflow management
│   │   ├── workflow.py          # LangGraph workflows
│   │   └── crews.py             # CrewAI configurations
│   └── mcp/                     # MCP tool integrations
├── tests/                       # Test suite
└── scripts/                     # Utility scripts
```

## Getting Started

### Prerequisites

- Python 3.11+
- Ollama (for local LLM inference)
- Docker (optional, for Qdrant)

### Installation

```bash
# Clone the repository
git clone https://github.com/lestinj/capability-assessment-framework.git
cd capability-assessment-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull Llama model (for development)
ollama pull llama3.1:70b
```

### Running Tests

```bash
pytest tests/
```

## Documentation

- [Architecture Overview](docs/architecture.md)
- [VDOT Retrospective POC](docs/retrospectives/vdot-retrospective.md)
- [VIPC Application Materials](docs/vipc-application/)

## Roadmap

### Phase 1: Proof of Concept (Current)
- [ ] VDOT retrospective analysis
- [ ] Basic document intake agent
- [ ] Simple RAG pipeline
- [ ] Assessment report generation

### Phase 2: MVP (Post-VIPC Funding)
- [ ] Multi-agent orchestration
- [ ] Qdrant vector store integration
- [ ] MCP tool connectors
- [ ] Web interface

### Phase 3: Production
- [ ] vLLM deployment
- [ ] SOC 2 compliance
- [ ] Enterprise integrations

## Contributing

This is currently a private development project. Contact the maintainer for collaboration opportunities.

## License

Proprietary — Xenon Enterprise Consulting, Inc.

## Contact

**Lestin P. Jackson, MBA**  
Principal, Xenon Enterprise Consulting  
Chesterfield, Virginia

---

*Project initialized: January 2026*
