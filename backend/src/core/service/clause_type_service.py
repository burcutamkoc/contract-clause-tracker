from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.infra.repository.clause_type_repository import ClauseTypeRepository
from src.infra.repository.entities.clause_type_entity import ClauseType


class ClauseTypeService:

    def __init__(self, db: Session = Depends(get_db)):

        self.repo = ClauseTypeRepository(db)

    def list_clause_types(self):

        return self.repo.all()

    def create_clause_type(self, name: str):

        clause = ClauseType(name=name)

        return self.repo.create(clause)