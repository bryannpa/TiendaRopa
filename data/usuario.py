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
