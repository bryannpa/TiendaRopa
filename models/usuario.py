from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: str

class UsuarioID(UsuarioBase):
    id: int
