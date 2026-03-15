from pydantic import BaseModel
from typing import Optional


class SentenceResponse(BaseModel):

    id: int
    contract_id: int
    text: str
    order: int

    class Config:
        from_attributes = True


class SentenceLabelRequest(BaseModel):

    clause_type_id: int

class SentenceWithLabel(BaseModel):

    id: int
    text: str
    order: int
    clause_type_id: Optional[int] = None
    clause_type_name: Optional[str] = None