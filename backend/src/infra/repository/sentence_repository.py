from sqlalchemy.orm import Session

from src.infra.repository.entities.sentence_entity import Sentence
from src.infra.repository.entities.sentence_label_entity import SentenceLabel
from src.infra.repository.entities.clause_type_entity import ClauseType


class SentenceRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, sentence: Sentence):

        self.db.add(sentence)
        self.db.commit()
        self.db.refresh(sentence)

        return sentence

    def get(self, sentence_id: int):

        return self.db.query(Sentence).filter(
            Sentence.id == sentence_id
        ).first()

    def get_by_contract(self, contract_id: int):

        results = (
            self.db.query(
                Sentence.id,
                Sentence.text,
                Sentence.order,
                ClauseType.id.label("clause_type_id"),
                ClauseType.name.label("clause_type_name")
            )
            .outerjoin(
                SentenceLabel,
                SentenceLabel.sentence_id == Sentence.id
            )
            .outerjoin(
                ClauseType,
                ClauseType.id == SentenceLabel.clause_type_id
            )
            .filter(Sentence.contract_id == contract_id)
            .order_by(Sentence.order)
            .all()
        )

        return results