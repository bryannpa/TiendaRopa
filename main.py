from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mi tienda de ropa"}