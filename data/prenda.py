import csv

from models.prenda import PrendaBase, PrendaID

data_base = "prenda.csv"
column_fields = ["id", "nombre", "tipo", "talla", "color", "precio", "cantidad"]

def auto_id():
    try:
        with open(data_base, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=column_fields)
            max_id = max(int(row["id"])for row in reader)
            return max_id + 1
    except (FileNotFoundError, ValueError):
        return auto_id()