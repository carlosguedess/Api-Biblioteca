# 📚 Api-Biblioteca

Uma API REST desenvolvida com **Python** e **FastAPI** para gerenciar livros, autores e empréstimos em uma biblioteca digital.

---

## 🚀 Funcionalidades

- 🔍 Listar livros disponíveis
- 📖 Cadastrar, editar e remover livros
- 👤 Gerenciar autores
- 📦 Registrar empréstimos e devoluções
- 🗃️ Integração com Supabase para persistência de dados

---

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
- [Supabase](https://supabase.com/) (banco de dados e autenticação)
- [Pydantic](https://docs.pydantic.dev/) (validação de dados)
- [Python 3.11+](https://www.python.org/)

---

## 📦 Instalação

```bash
# Clonar o repositório
git clone https://github.com/carlosguedes/api-biblioteca.git

# Entrar na pasta do projeto
cd api-biblioteca

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instalar dependências
pip install -r requirements.txt

#Executar o Porjeto
uvicorn main:app --reload
