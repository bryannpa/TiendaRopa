from pydantic import BaseModel

class Prenda(BaseModel):
    nombre: str
    tipo: str
    talla: str
    precio: float
    cantidad: int

class PrendaID(PrendaBase):
    id : int
