from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    telefono: str

class Usuario(UsuarioBase):
    id: int
