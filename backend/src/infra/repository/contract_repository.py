from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import func

from src.infra.repository.entities.contract_entity import Contract
from src.infra.repository.entities.sentence_entity import Sentence
from src.infra.repository.entities.sentence_label_entity import SentenceLabel


class ContractRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, contract: Contract):
        self.db.add(contract)
        self.db.commit()
        self.db.refresh(contract)
        return contract

    def delete(self, contract_id: int):

        contract = self.db.query(Contract).filter(
            Contract.id == contract_id
        ).first()

        if not contract:
            return None

        self.db.delete(contract)
        self.db.commit()

        return contract

    def all(
        self,
        search: Optional[str] = None,
        status: Optional[str] = None
    ):
        sentence_count = func.count(Sentence.id).label("sentence_count")
        labeled_count = func.count(SentenceLabel.id).label("labeled_count")

        query = (
            self.db.query(
                Contract,
                sentence_count,
                labeled_count,
            )
            .outerjoin(Sentence, Sentence.contract_id == Contract.id)
            .outerjoin(SentenceLabel, SentenceLabel.sentence_id == Sentence.id)
        )

        if search:
            query = query.filter(Contract.name.ilike(f"%{search}%"))

        query = query.group_by(Contract.id)

        if status == "completed":
            query = query.having(func.count(Sentence.id) > 0)
            query = query.having(func.count(SentenceLabel.id) == func.count(Sentence.id))
        elif status == "in_progress":
            query = query.having(func.count(SentenceLabel.id) > 0)
            query = query.having(func.count(SentenceLabel.id) < func.count(Sentence.id))
        elif status == "not_started":
            query = query.having(func.count(SentenceLabel.id) == 0)

        return query.all()

    def get(self, contract_id: int):

        return self.db.query(Contract).filter(
            Contract.id == contract_id
        ).first()