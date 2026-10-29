from fastapi import APIRouter, status, HTTPException
from models.compra import CompraID, CompraBase, CompraRespuesta
from data.compra import crear_compra, read_all_compras
from data.prenda import read_prenda
from data.usuario import read_all_usuarios
from data.vendedor import read_all_vendedores

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompraID)
def regitrar_compra(compra: CompraBase):
    usuarios = read_all_usuarios()
    prenda = read_prenda()

    usuario_existe = False

    for usuario in usuarios:
        if usuario.id == compra.usuario_id:
            usuario_existe = True
            break

    if not usuario_existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="el usuario no existe")

    vendedor_id = 0
    prenda_existe = False

    for prenda in prenda:
        if prenda.id == compra.prenda_id:
            vendedor_id = prenda.vendedor_id
            prenda_existe = True
            break

    if not prenda_existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="prenda no existe")

    compra_con_vendedor = CompraBase(
        usuario_id=compra.usuario_id,
        prenda_id=compra.prenda_id,
        vendedor_id=vendedor_id,
        cantidad=compra.cantidad
    )

    return crear_compra(compra_con_vendedor)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompraRespuesta])
def mostrar_compra():
    compras = read_all_compras()
    usuarios = read_all_usuarios()
    prenda = read_prenda()
    vendedores = read_all_vendedores()

    resultados = []

    for compra in compras:
        nombre_usuario = "desconocido"
        nombre_prenda = "desconocido"
        nombre_vendedor = "desconocido"

        for usuario in usuarios:
            if usuario.id == compra.usuario_id:
                nombre_usuario = usuario.nombre + " " + usuario.apellido
                break

        for prenda in prenda:
            if prenda.id == compra.prenda_id:
                nombre_prenda = (prenda.tipo + " " + prenda.color + ", talla" + prenda.talla)
                break

        for vendedor in vendedores:
            if vendedor.id == compra.vendedor_id:
                nombre_vendedor = vendedor.nombre + " " + vendedor.apellido
                break

        respuesta = CompraRespuesta(
            id=compra.id,
            usuario_id=compra.usuario_id,
            usuario=nombre_usuario,
            prenda_id=compra.prenda_id,
            prenda=nombre_prenda,
            vendedor_id=compra.vendedor_id,
            vendedor=nombre_vendedor,
            cantidad=compra.cantidad
        )

        resultados.append(respuesta)

    return resultados
