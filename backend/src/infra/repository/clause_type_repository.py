from sqlalchemy.orm import Session

from src.infra.repository.entities.clause_type_entity import ClauseType


class ClauseTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def all(self):
        """
        Returns all clause type records.
        """
        return self.db.query(ClauseType).all()

    def get(self, clause_type_id: int):
        """
        Retrieves a clause type by ID.
        """
        return self.db.query(ClauseType).filter(
            ClauseType.id == clause_type_id
        ).first()

    def create(self, clause_type: ClauseType):
        """
        Creates a new clause type.
        """
        self.db.add(clause_type)
        self.db.commit()
        self.db.refresh(clause_type)

        return clause_type