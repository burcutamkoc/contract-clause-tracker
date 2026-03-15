from sqlalchemy.orm import Session

from src.infra.repository.entities.sentence_label_entity import SentenceLabel


class LabelRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, label: SentenceLabel):

        self.db.add(label)
        self.db.commit()
        self.db.refresh(label)

        return label