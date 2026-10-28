from fastapi import FastAPI
from routers import prenda

app = FastAPI()

app.include_router(
    router=prenda.router,
    prefix="/prenda",
    tags=["prenda"],
)