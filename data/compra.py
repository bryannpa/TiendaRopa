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