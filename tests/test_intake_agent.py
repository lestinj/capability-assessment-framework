"""
Tests for the Intake Agent

These tests verify document classification, text extraction,
chunking, and embedding generation functionality.
"""

import pytest
from src.agents.intake_agent import IntakeAgent, DocumentType, TextChunk


class TestIntakeAgent:
    """Test suite for IntakeAgent."""
    
    @pytest.fixture
    def agent(self):
        """Create a configured IntakeAgent instance."""
        config = {
            'supported_formats': ['pdf', 'docx', 'xlsx'],
            'chunk_size': 512,
            'chunk_overlap': 50,
        }
        return IntakeAgent(config)
    
    def test_agent_initialization(self, agent):
        """Test that agent initializes with correct config."""
        assert agent.supported_formats == ['pdf', 'docx', 'xlsx']
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_classify_policy_document(self, agent):
        """Test classification of a policy document."""
        # TODO: Implement when classify_document is ready
        result = agent.classify_document("test_data/sample_policy.pdf")
        assert result == DocumentType.POLICY
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_classify_architecture_diagram(self, agent):
        """Test classification of an architecture diagram."""
        # TODO: Implement when classify_document is ready
        result = agent.classify_document("test_data/architecture.pdf")
        assert result == DocumentType.ARCHITECTURE_DIAGRAM
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_extract_text_pdf(self, agent):
        """Test text extraction from PDF."""
        # TODO: Implement when extract_text is ready
        text = agent.extract_text("test_data/sample.pdf")
        assert len(text) > 0
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_chunk_text(self, agent):
        """Test text chunking."""
        # TODO: Implement when chunk_text is ready
        sample_text = "This is a sample text. " * 100
        chunks = agent.chunk_text(sample_text, "doc_001")
        
        assert len(chunks) > 0
        assert all(isinstance(c, TextChunk) for c in chunks)
        assert all(c.document_id == "doc_001" for c in chunks)
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_generate_embeddings(self, agent):
        """Test embedding generation."""
        # TODO: Implement when generate_embeddings is ready
        chunks = [
            TextChunk(content="Sample text", document_id="doc_001", chunk_index=0, metadata={})
        ]
        result = agent.generate_embeddings(chunks)
        
        assert len(result) == 1
        assert result[0].embedding is not None
        assert len(result[0].embedding) == 1024  # BGE dimension


class TestDocumentType:
    """Test DocumentType enum."""
    
    def test_document_types_exist(self):
        """Verify all expected document types exist."""
        expected_types = [
            'POLICY',
            'ARCHITECTURE_DIAGRAM', 
            'SYSTEM_INVENTORY',
            'PROCESS_DOCUMENT',
            'STANDARDS',
            'ROADMAP',
            'ASSESSMENT',
            'UNKNOWN',
        ]
        for type_name in expected_types:
            assert hasattr(DocumentType, type_name)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
