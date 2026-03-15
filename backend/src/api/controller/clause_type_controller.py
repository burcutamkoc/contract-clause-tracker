from fastapi import APIRouter, Depends

from src.core.service.clause_type_service import ClauseTypeService
from typing import List
from src.core.models.clause_type import ClauseTypeResponse

router = APIRouter(prefix="/clause-types", tags=["clause-types"])


@router.get("", response_model=List[ClauseTypeResponse])
def list_clause_types(
    service: ClauseTypeService = Depends()
):

    return service.list_clause_types()

@router.post("")
def create_clause_type(name: str, service: ClauseTypeService = Depends()):

    return service.create_clause_type(name)