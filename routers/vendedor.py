from fastapi import APIRouter, status
from models.vendedor import VendedorBase, VendedorID
from data.vendedor import crear_vendedor, read_all_vendedores

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VendedorID)
def registrar_vendedor(vendedor: VendedorBase):
    return crear_vendedor(vendedor)

@router.get("/",status_code=status.HTTP_200_OK, response_model=list[VendedorID])
def mostrar_vendedores():
    return read_all_vendedores()