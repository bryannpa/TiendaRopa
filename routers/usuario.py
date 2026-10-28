from fastapi import APIRouter, status
from models.usuario import UsuarioID,UsuarioBase
from  data.usuario import crearar_usuario, read_all_usuarios

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UsuarioID)
def mostrar_usuario(usuario: UsuarioBase):
    return crearar_usuario(usuario)


