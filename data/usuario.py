import csv

from data.prenda import data_base, column_fields
from models.usuario import  UsuarioBase, UsuarioID

data_base = "usuario.csv"
column_fields = ["id", "nombre", "apellido", "correo", "telefono"]

def auto_id():
    try:
        with open (data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            max_id = max(int(row["id"])for row in reader)
    except (FileNotFoundError, ValueError):
        return 1

def write_usuario_into_csv(resgistrar: UsuarioID):
    with open(data_base, mode="a", newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writerow(resgistrar.model_dump())

def crearar_usuario(usuario: UsuarioBase):
    new_id = auto_id()
    new_usuario_ID = UsuarioID(id=new_id, **usuario.model_dump())
    write_usuario_into_csv(new_usuario_ID)
    return new_usuario_ID

def read_all_usuarios():
    try:
        with open(data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            return [UsuarioID(**row)for row in reader]
    except FileNotFoundError:
        return []
