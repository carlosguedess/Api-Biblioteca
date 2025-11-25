from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase
from app.models import Livros

router = APIRouter(prefix="/livros")

@router.get("/")
def listar():
    data = supabase.table("livros").select("*").execute()
    return data.data

@router.get("/{id}")
def buscar(id: int):
    data = supabase.table("livros").select("*").eq("id", id).execute()
    if not data.data:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return data.data[0]

@router.post("/")
def criar(livro: Livros):
    data = supabase.table("livros").insert(livro.dict()).execute()
    return data.data[0]

@router.put("/{id}")
def atualizar(id: int, livro: Livros):
    data = supabase.table("livros").update(livro.dict()).eq("id", id).execute()
    return data.data

@router.delete("/{id}")
def excluir(id: int):
    supabase.table("livros").delete().eq("id", id).execute()
    return {"message": "Livro excluído com sucesso"}