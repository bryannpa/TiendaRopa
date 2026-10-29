from pydantic import BaseModel

class VendedorBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: str

class VendedorID(VendedorBase):
    id: int