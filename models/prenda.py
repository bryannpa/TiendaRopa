from pydantic import BaseModel

class PrendaBase(BaseModel):
    nombre: str
    tipo: str
    talla: str
    precio: float
    cantidad: int
    color: str

class PrendaID(PrendaBase):
    id : int
