# Capability Assessment Framework - Claude Context

This file provides context for Claude AI when working on this project.

## Project Overview

**What we're building:** An AI-driven platform that automates enterprise architecture capability assessments, reducing what typically takes consulting firms 24+ weeks and $500K-$2M down to ~2 weeks at a fraction of the cost.

**Business context:** Xenon Enterprise Consulting is applying for a $250K VIPC (Virginia Innovation Partnership Corporation) grant to commercialize this platform. We need to demonstrate a working proof of concept.

**Current phase:** Building a retrospective POC using the VDOT (Virginia Department of Transportation) engagement as a case study.

## Tech Stack Decisions

### Agent Orchestration
- **LangGraph** for complex, stateful workflows with auditability
- **CrewAI** for multi-agent collaboration with role-based agents

### LLM
- **Development:** Llama 3.1 70B via Ollama
- **Production:** Llama 3.1 70B via vLLM
- **Rationale:** Open source, Apache 2.0 license, can run on-premises for government clients

### RAG Stack
- **Embeddings:** bge-large-en-v1.5 (or gte-large)
- **Vector DB:** Qdrant
- **Reranker:** bge-reranker-v2-m3

### Enterprise Integration
- **MCP (Model Context Protocol)** for tool interfaces
- REST APIs for external systems (ServiceNow, CMDB, etc.)

## Coding Standards

- **Python version:** 3.11+
- **Type hints:** Required on all functions
- **Docstrings:** Google style, required for all public functions
- **Testing:** pytest, aim for >80% coverage on core logic
- **Formatting:** Black, isort
- **Linting:** Ruff

## Key Concepts

| Term | Definition |
|------|------------|
| Assessment | A full enterprise architecture capability evaluation |
| Agent | A specialized AI worker (intake, discovery, assessment, reporting) |
| Crew | A coordinated group of agents working together |
| Capability | A business or technical function (e.g., "Data Governance") |
| Maturity Level | CMM-style 1-5 rating of capability maturity |

## Agent Roles

1. **Intake Agent** — Receives documents, classifies them, extracts metadata
2. **Discovery Agent** — Identifies capabilities, technologies, dependencies from documents
3. **Assessment Agent** — Evaluates capabilities against frameworks (TOGAF, CMMI, etc.)
4. **Reporting Agent** — Generates assessment reports, roadmaps, visualizations

## Project Priorities

1. **VDOT Retrospective POC** — Demonstrate value with real case study
2. **VIPC Application** — Complete grant application with POC evidence
3. **Agent Development** — Build working agents iteratively
4. **Documentation** — Keep architecture docs current

## File Organization

When creating new files:
- Agents go in `src/agents/`
- RAG components go in `src/rag/`
- Workflow/orchestration in `src/orchestration/`
- MCP tools in `src/mcp/`
- Tests mirror src structure in `tests/`
- Documentation in `docs/`

## Important Notes

- The Air Force contract mentioned in early documents was a **proposal example**, not awarded work
- Focus on Virginia state agencies for VIPC alignment
- All development should support the grant narrative of "validated prototype"

## Founder Context

**Lestin P. Jackson, MBA**
- 20+ years enterprise architecture experience
- Fortune 500: Disney, Hertz (Senior Director), Blue Cross Blue Shield
- Government: CMS, VDOT, VA DSS (established EA practice)
- Certifications: TOGAF, AWS Solutions Architect Professional
- Location: Chesterfield, Virginia
