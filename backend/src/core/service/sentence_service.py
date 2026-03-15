from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from src.core.models.sentence import SentenceWithLabel
from src.core.database import get_db
from src.infra.repository.sentence_repository import SentenceRepository
from src.infra.repository.label_repository import LabelRepository
from src.infra.repository.entities.sentence_label_entity import SentenceLabel


class SentenceService:

    def __init__(self, db: Session = Depends(get_db)):

        self.repo = SentenceRepository(db)
        self.label_repo = LabelRepository(db)

    def get_sentences_by_contract(self, contract_id: int):

        rows = self.repo.get_by_contract(contract_id)
        
        return [
            SentenceWithLabel(
                id=r.id,
                text=r.text,
                order=r.order,
                clause_type_id=r.clause_type_id,
                clause_type_name=r.clause_type_name
            )
            for r in rows
        ]
    def label_sentence(self, sentence_id: int, clause_type_id: int):

        sentence = self.repo.get(sentence_id)

        if not sentence:
            raise HTTPException(status_code=404, detail="Sentence not found")

        label = SentenceLabel(
            sentence_id=sentence_id,
            clause_type_id=clause_type_id
        )

        return self.label_repo.create(label)