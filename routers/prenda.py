from fastapi import APIRouter, status
from models.prenda import PrendaBase, PrendaID
from data.prenda import crear_prenda, read_prenda

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PrendaID)
def registar_prenda(prerenda: PrendaBase):
    return crear_prenda(prerenda)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PrendaID])
def mostrar_prenda():
    return read_prenda()