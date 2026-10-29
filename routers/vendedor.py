from fastapi import APIRouter, status
from models.vendedor import VendedorBase, VendedorID
from data.vendedor import crear_vendedor, read_all_vendedores

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VendedorID)
def registrar_vendedor(vendedor: VendedorBase):
    return registrar_vendedor(vendedor)