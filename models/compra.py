from pydantic import BaseModel

class CompraBase(BaseModel):
    usuario_id: int
    prenda_id: int
    cantidad: int

class CompraID(CompraBase):
    id: int
