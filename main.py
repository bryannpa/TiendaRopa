from fastapi import FastAPI
from routers import prenda, usuario

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