from fastapi import APIRouter, Depends
from typing import List

from src.core.service.sentence_service import SentenceService
from src.core.models.sentence import SentenceLabelRequest, SentenceWithLabel

router = APIRouter(tags=["sentences"])


@router.get(
    "/contracts/{contract_id}/sentences",
    response_model=List[SentenceWithLabel]
)
def list_sentences(
    contract_id: int,
    service: SentenceService = Depends()
):
    return service.get_sentences_by_contract(contract_id)


@router.post("/sentences/{sentence_id}/label")
def label_sentence(
    sentence_id: int,
    body: SentenceLabelRequest,
    service: SentenceService = Depends()
):
    return service.label_sentence(
        sentence_id=sentence_id,
        clause_type_id=body.clause_type_id
    )