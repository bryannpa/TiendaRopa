from fastapi import FastAPI
from routers import prenda, usuario, vendedor, compra

app = FastAPI()

app.include_router(
    router=prenda.router,
    prefix="/prenda",
    tags=["prenda"],
)

app.include_router(
    router=usuario.router,
    prefix="/usuario",
    tags=["usuario"],
)

app.include_router(
    router=vendedor.router,
    prefix="/vendedor",
    tags=["vendedor"],
)

app.include_router(
    router=compra.router,
    prefix="/compras",
    tags=["compras"],
)