from pydantic import BaseModel

class VendediroBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: str

class VendedorID(VendediroBase):
    id: int