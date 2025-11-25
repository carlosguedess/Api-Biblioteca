from pydantic import BaseModel

class Livros(BaseModel):
    #id: int
    title: str
    autor: str
    ano: int
    disponivel: bool = True