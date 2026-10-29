import csv

from models.prenda import PrendaBase, PrendaID

data_base = "prendas.csv"
column_fields = ["id", "tipo", "talla", "precio", "cantidad", "color", "vendedor_id"]

def auto_id():
    try:
        with open(data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            max_id = max(int(row["id"])for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return 1

def write_prenda_into_csv(registrar: PrendaID):
    with open(data_base, mode="a", newline="",encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_fields)
        writer.writerow(registrar.model_dump())

def crear_prenda(prenda: PrendaBase):
    new_id = auto_id()
    new_prenda_id = PrendaID(id=new_id, **prenda.model_dump())
    write_prenda_into_csv(new_prenda_id)
    return new_prenda_id

def read_prenda():
    try:
        with open(data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            prendas = []

            for row in reader:
                prenda = PrendaID(
                    id=int(row["id"]),
                    tipo=row["tipo"],
                    talla=row["talla"],
                    precio=float(row["precio"]),
                    cantidad=int(row["cantidad"]),
                    color=row["color"],
                    vendedor_id=int(row["vendedor_id"]),
                )
                prendas.append(prenda)
            return prendas

    except FileNotFoundError:
        return []



