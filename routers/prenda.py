from fastapi import APIRouter, status, HTTPException
from models.prenda import PrendaBase, PrendaID
from data.prenda import crear_prenda, read_prenda
from data.vendedor import read_all_vendedores

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PrendaID)
def registar_prenda(prerenda: PrendaBase):
    vendedores = read_all_vendedores()

    vendedor_existe = False

    for vendedor in vendedores:
        if vendedor.id == prerenda.vendedor_id:
            vendedor_existe = True


    if not vendedor_existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="el vendedor no existe")

    return crear_prenda(prerenda)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PrendaID])
def mostrar_prenda():
    return read_prenda()