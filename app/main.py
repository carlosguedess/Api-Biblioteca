from fastapi import FastAPI
from app.routers import livros

app = FastAPI(title="API de Biblioteca")

app.include_router(livros.router)

@app.get("/")
def inicio():
    return {"Status": "A nossa API de Biblioteca está funcionando!"}