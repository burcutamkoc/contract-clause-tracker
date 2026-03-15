from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class SentenceLabel(Base):
    __tablename__ = "sentence_labels"

    id = Column(Integer, primary_key=True, index=True)

    sentence_id = Column(Integer, ForeignKey("sentences.id"))

    clause_type_id = Column(Integer, ForeignKey("clause_types.id"))

    sentence = relationship("Sentence", back_populates="labels")