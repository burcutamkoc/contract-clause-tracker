from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.core.database import Base


class Sentence(Base):
    __tablename__ = "sentences"

    id = Column(Integer, primary_key=True, index=True)

    contract_id = Column(Integer, ForeignKey("contracts.id"))

    text = Column(Text, nullable=False)

    order = Column(Integer)

    contract = relationship("Contract", back_populates="sentences")

    labels = relationship("SentenceLabel", back_populates="sentence")