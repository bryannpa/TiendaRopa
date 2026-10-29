import csv

from data.prenda import column_fields
from models.vendedor import VendedorBase, VendedorID

data_base = "vendedor.csv"
column_fields = ["id", " nombre", "apellido", "correo", "telefono"]

def  auto_id():
    try:
        with open(data_base,"r", newline="",encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            max_id = max (int(row["id"])for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1

def write_vendedor_into_csv(registrar: VendedorID):
    with open (data_base, mode="a",newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writerow(registrar.model_dump())

def crear_vendedor(vendedor: VendedorBase):
    new_id = auto_id()
    new_vendedor_ID = VendedorID(id=new_id, **vendedor.model_dump())
    write_vendedor_into_csv(new_vendedor_ID)
    return new_vendedor_ID

def read_all_vendedores():
    try:
        with open(data_base,"r",newline="",encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            return [VendedorBase(**row) for row in reader]
    except FileNotFoundError:
        return []