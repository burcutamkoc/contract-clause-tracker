from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from src.core.database import get_db

from src.infra.repository.contract_repository import ContractRepository
from src.infra.repository.sentence_repository import SentenceRepository

from src.infra.repository.entities.contract_entity import Contract
from src.infra.repository.entities.sentence_entity import Sentence
from src.core.models.contract import ContractDashboard
from src.core.service.sentence_parser import split_into_sentences


class ContractService:

    def __init__(self, db: Session = Depends(get_db)):

        self.repo = ContractRepository(db)

        self.sentence_repo = SentenceRepository(db)

    # def list_contracts(self):

    #     results = self.repo.all()

    #     return [
    #         ContractDashboard(
    #             id=contract.id,
    #             name=contract.name,
    #             sentence_count=sentence_count,
    #             labeled_count=labeled_count,
    #             created_at = contract.created_at
    #         )
    #         for contract, sentence_count, labeled_count in results
    #     ]

    def list_contracts(self, status: str | None = None, search: str | None = None):

        results = self.repo.all(search=search, status=status)

        return [
            ContractDashboard(
                id=contract.id,
                name=contract.name,
                sentence_count=sentence_count,
                labeled_count=labeled_count,
                created_at=contract.created_at,
                status=(
                    "completed" if labeled_count == sentence_count and sentence_count > 0
                    else "in_progress" if labeled_count > 0
                    else "not_started"
                )
            )
            for contract, sentence_count, labeled_count in results
        ]

    def get_contract(self, contract_id: int):

        contract = self.repo.get(contract_id)

        if not contract:
            raise HTTPException(404, "Contract not found")

        return contract

    def create_contract(self, name: str, content: str):

        contract = Contract(
            name=name,
            content=content,
            created_at=datetime.utcnow()
        )

        contract = self.repo.create(contract)

        sentences = split_into_sentences(content)

        for index, text in enumerate(sentences):

            sentence = Sentence(
                contract_id=contract.id,
                text=text,
                order=index
            )

            self.sentence_repo.create(sentence)

        return contract

    def delete_contract(self, contract_id: int):

        contract = self.repo.delete(contract_id)

        if not contract:
            raise HTTPException(404, "Contract not found")

        return contract