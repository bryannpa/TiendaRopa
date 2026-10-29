from fastapi import APIRouter, status
from models.compra import CompraID,CompraBase
from data.compra import crear_compra, read_all_compras

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompraID)
def regitrar_compra(compra: CompraBase):
    return crear_compra(compra)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompraID])
def mostrar_compra():
    return read_all_compras()