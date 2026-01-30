"""
CAF Agents Module

This module contains the specialized AI agents that power the
Capability Assessment Framework:

- IntakeAgent: Document classification and processing
- DiscoveryAgent: Capability and technology discovery
- AssessmentAgent: Maturity evaluation and gap analysis
- ReportingAgent: Report and visualization generation
"""

from .intake_agent import IntakeAgent, DocumentType, Document, TextChunk
from .discovery_agent import DiscoveryAgent, Capability, Technology, Dependency
from .assessment_agent import AssessmentAgent, MaturityLevel, MaturityScore, Gap, Risk, Recommendation
from .reporting_agent import ReportingAgent, ReportFormat, Visualization, Roadmap

__all__ = [
    # Agents
    'IntakeAgent',
    'DiscoveryAgent', 
    'AssessmentAgent',
    'ReportingAgent',
    # Data classes
    'DocumentType',
    'Document',
    'TextChunk',
    'Capability',
    'Technology',
    'Dependency',
    'MaturityLevel',
    'MaturityScore',
    'Gap',
    'Risk',
    'Recommendation',
    'ReportFormat',
    'Visualization',
    'Roadmap',
]
