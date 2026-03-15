from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from src.core.service.contract_service import ContractService
from src.core.models.contract import ContractCreate
from src.core.models.contract import ContractDashboard
from src.core.models.contract import ContractResponse
from fastapi import UploadFile, File


router = APIRouter(prefix="/contracts", tags=["contracts"])


@router.get("", response_model=List[ContractDashboard])
def list_contracts(
    status: Optional[str] = None,
    search: Optional[str] = None,
    service: ContractService = Depends()
):
    return service.list_contracts(status=status, search=search)

@router.get("/{contract_id}", response_model=ContractResponse)
def get_contract(
    contract_id: int,
    service: ContractService = Depends()
):

    return service.get_contract(contract_id)


@router.post("")
def create_contract(
    contract: ContractCreate,
    service: ContractService = Depends()
):

    return service.create_contract(
        contract.name,
        contract.content
    )

@router.post("/upload", response_model=ContractResponse)
async def upload_contract(
    file: UploadFile = File(...),
    service: ContractService = Depends()
):

    if not file.filename.endswith((".txt", ".md")):
        raise HTTPException(400, "Only .txt or .md files are supported")

    content = await file.read()
    text = content.decode("utf-8")

    return service.create_contract(file.filename, text)

@router.delete("/{contract_id}", response_model=ContractResponse)
def delete_contract(
    contract_id: int,
    service: ContractService = Depends()
):

    return service.delete_contract(contract_id)

