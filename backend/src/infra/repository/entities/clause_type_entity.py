from sqlalchemy import Column, Integer, String

from src.core.database import Base


class ClauseType(Base):
    __tablename__ = "clause_types"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)