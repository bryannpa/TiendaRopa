from fastapi import APIRouter, status, HTTPException
from models.prenda import PrendaBase, PrendaID, PrendaRespuesta
from data.prenda import crear_prenda, read_prenda
from data.vendedor import read_all_vendedores

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PrendaRespuesta)
def registar_prenda(prerenda: PrendaBase):
    vendedores = read_all_vendedores()

    vendedor_encontrado = None

    for vendedor in vendedores:
        if vendedor.id == prerenda.vendedor_id:
            vendedor_encontrado = vendedor
            break


    if  vendedor_encontrado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="el vendedor no existe")
    nueva_prenda = crear_prenda(prerenda)
    return PrendaRespuesta(**nueva_prenda.model_dump(), nombre_vendedor=vendedor_encontrado.nombre)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PrendaID])
def mostrar_prenda():
    prendas = read_prenda()
    vendedores = read_all_vendedores()

    resultados = []

    for prenda in prendas:
        nombre_vendedor = "desconocido"

        for vendedor in vendedores:
            if vendedor.id == prenda.vendedor_id:
                nombre_vendedor = vendedor.nombre
                break

        prenda_respuesta = PrendaRespuesta(**prenda.model_dump(),nombre_vendedor=nombre_vendedor)
        resultados.append(prenda_respuesta)
        return resultados