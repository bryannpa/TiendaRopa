from pydantic import BaseModel

class CompraBase(BaseModel):
    usuario_id: int
    prenda_id: int
    vendedor_id: int
    cantidad: int

class CompraID(CompraBase):
    id: int

class CompraRespuesta(BaseModel):
    id: int
    usuario_id: int
    usuario: str
    prenda_id: int
    prenda: str
    vendedor_id: int
    vendedor: str
    cantidad: int
