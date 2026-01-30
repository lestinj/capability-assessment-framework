# Capability Assessment Framework - Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        CAF Platform                                  │
├─────────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │   Document   │  │   Web UI     │  │   API        │              │
│  │   Upload     │  │   Dashboard  │  │   Gateway    │              │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │
│         │                 │                  │                      │
│         └─────────────────┼──────────────────┘                      │
│                           ▼                                         │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                  Orchestration Layer                         │   │
│  │              (LangGraph + CrewAI)                           │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │                                       │
│         ┌───────────────────┼───────────────────┐                  │
│         ▼                   ▼                   ▼                   │
│  ┌────────────┐     ┌────────────┐      ┌────────────┐             │
│  │  Intake    │     │ Discovery  │      │ Assessment │             │
│  │  Agent     │────▶│ Agent      │─────▶│ Agent      │             │
│  └────────────┘     └────────────┘      └─────┬──────┘             │
│                                               │                     │
│                                               ▼                     │
│                                        ┌────────────┐              │
│                                        │ Reporting  │              │
│                                        │ Agent      │              │
│                                        └────────────┘              │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      RAG Layer                               │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │   │
│  │  │Embeddings│  │ Qdrant   │  │ Retriever│  │ Reranker │    │   │
│  │  │  (BGE)   │  │ Vector DB│  │          │  │  (BGE)   │    │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                      LLM Layer                               │   │
│  │              Llama 3.1 70B (Ollama / vLLM)                  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    MCP Tool Layer                            │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │   │
│  │  │ServiceNow│  │  CMDB    │  │  Ardoq   │  │  Custom  │    │   │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Orchestration Layer

**LangGraph** manages the overall assessment workflow:
- Stateful graph-based execution
- Checkpoint/resume capability
- Audit trail for compliance
- Conditional branching based on document types

**CrewAI** coordinates multi-agent collaboration:
- Role-based agent definitions
- Task delegation and handoff
- Consensus mechanisms for assessments

### 2. Agent Layer

#### Intake Agent
**Purpose:** Receive and classify incoming documents

**Inputs:**
- Raw documents (PDF, DOCX, XLSX, Visio, etc.)
- User context (organization, project scope)

**Outputs:**
- Classified document metadata
- Extracted text chunks
- Document embeddings stored in Qdrant

**Key Functions:**
```python
- classify_document(doc) -> DocumentType
- extract_text(doc) -> List[TextChunk]
- identify_entities(text) -> List[Entity]
- store_embeddings(chunks) -> None
```

#### Discovery Agent
**Purpose:** Identify capabilities, technologies, and dependencies

**Inputs:**
- Classified documents from Intake Agent
- RAG context from vector store
- Framework definitions (TOGAF, CMMI, etc.)

**Outputs:**
- Capability inventory
- Technology catalog
- Dependency map
- Organizational structure

**Key Functions:**
```python
- discover_capabilities(docs) -> List[Capability]
- map_technologies(docs) -> List[Technology]
- identify_dependencies(capabilities) -> DependencyGraph
- extract_org_structure(docs) -> OrgChart
```

#### Assessment Agent
**Purpose:** Evaluate capabilities against maturity frameworks

**Inputs:**
- Capability inventory from Discovery Agent
- Assessment framework (CMMI, TOGAF, custom)
- Historical assessments (if available)

**Outputs:**
- Maturity scores (1-5 scale)
- Gap analysis
- Risk identification
- Improvement recommendations

**Key Functions:**
```python
- assess_maturity(capability, framework) -> MaturityScore
- identify_gaps(current, target) -> List[Gap]
- evaluate_risks(gaps) -> List[Risk]
- recommend_improvements(gaps) -> List[Recommendation]
```

#### Reporting Agent
**Purpose:** Generate assessment deliverables

**Inputs:**
- Assessment results from Assessment Agent
- Report templates
- Visualization preferences

**Outputs:**
- Executive summary
- Detailed assessment report
- Transformation roadmap
- Visualizations (heatmaps, dependency diagrams)

**Key Functions:**
```python
- generate_executive_summary(results) -> Document
- create_detailed_report(results) -> Document
- build_roadmap(recommendations) -> Roadmap
- create_visualizations(data) -> List[Chart]
```

### 3. RAG Layer

**Embeddings (BGE-large-en-v1.5)**
- 1024-dimensional vectors
- Optimized for retrieval tasks
- Run locally for data privacy

**Vector Store (Qdrant)**
- Persistent storage for document embeddings
- Efficient similarity search
- Metadata filtering
- Collection per organization/project

**Retriever**
- Hybrid search (dense + sparse)
- Configurable top-k
- Context window management

**Reranker (BGE-reranker-v2-m3)**
- Cross-encoder reranking
- Improves retrieval precision
- Applied after initial retrieval

### 4. LLM Layer

**Development:** Ollama with Llama 3.1 70B
- Local inference
- No data leaves environment
- Fast iteration

**Production:** vLLM with Llama 3.1 70B
- Optimized inference
- Batch processing
- Horizontal scaling

### 5. MCP Tool Layer

Model Context Protocol enables standardized integration with enterprise tools:

- **ServiceNow** — Incident/change data, service catalog
- **CMDB** — Configuration items, relationships
- **Ardoq** — EA repository integration
- **Custom** — Organization-specific tools

## Data Flow

```
1. User uploads documents
   │
   ▼
2. Intake Agent classifies and chunks documents
   │
   ▼
3. Embeddings stored in Qdrant
   │
   ▼
4. Discovery Agent queries RAG, identifies capabilities
   │
   ▼
5. Assessment Agent evaluates against framework
   │
   ▼
6. Reporting Agent generates deliverables
   │
   ▼
7. User reviews and exports results
```

## Security Considerations

- **Data Privacy:** All processing on-premises / private cloud
- **Access Control:** Role-based access to assessments
- **Audit Trail:** Complete logging of agent actions
- **Encryption:** At-rest and in-transit encryption
- **Compliance:** Designed for SOC 2, FedRAMP readiness

## Scalability

- **Horizontal:** Multiple vLLM instances behind load balancer
- **Vertical:** GPU acceleration for inference
- **Storage:** Qdrant clustering for large document sets
- **Async:** Background processing for long assessments
