from pydantic import BaseModel
from datetime import datetime


class ContractCreate(BaseModel):

    name: str
    content: str


class ContractResponse(BaseModel):

    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class ContractDashboard(BaseModel):

    id: int
    name: str
    sentence_count: int
    labeled_count: int
    created_at: datetime
    status: str