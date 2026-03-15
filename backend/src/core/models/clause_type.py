from pydantic import BaseModel


class ClauseTypeResponse(BaseModel):

    id: int
    name: str

    class Config:
        from_attributes = True


class ClauseTypeCreate(BaseModel):

    name: str