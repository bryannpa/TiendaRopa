import csv

from data.prenda import column_fields
from models.compra import  CompraBase, CompraID

data_base = "compras.csv"
column_fields = ["id", "usuario_id", "prenda_id", "cantidad"]

def auto_id():
    try:
        with open(data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            max_id = max(int(row["id"])for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1

def write_compra_into_csv(registrar: CompraID):
    with open(data_base, mode="a", newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writerow(registrar.model_dump())

def crear_compra(compra: CompraBase):
    new_id = auto_id()
    new_compra_ID = CompraID(id=new_id, **compra.model_dump())
    write_compra_into_csv(new_compra_ID)
    return new_compra_ID

def read_all_compras():
    try:
        with open(data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            return [CompraID(**row)for row in reader]
    except FileNotFoundError:
        return []