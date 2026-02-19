from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import UserDefinedType
from sqlalchemy.dialects.postgresql import UUID, JSONB

Base = declarative_base()

class Vector(UserDefinedType):
    def get_col_spec(self, **kw):
        return "vector(1024)"
    
class DocumentChunkModel(Base):
    __tablename__ = "document_chunks"
    id =  Column(UUID(as_uuid=True), primary_key=True)
    document_id = Column(UUID(as_uuid=True), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    chunk_text = Column(Text, nullable=False)
    embedding = Column(Vector)
    metadata = Column(JSONB)
