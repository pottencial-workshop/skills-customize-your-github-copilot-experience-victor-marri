"""FastAPI Starter Code for Assignment: Construindo APIs REST com FastAPI

Execute com:
    uvicorn starter-code:app --reload

Objetivos principais:
- Rota de saúde (/health)
- CRUD de livros
- Filtro por autor
- Uso de modelos Pydantic e response_model
- Exemplo de dependência simples para logging/tempo
"""
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel, Field
import time

app = FastAPI(title="Mergington High School - FastAPI Assignment",
              description="API exemplo para prática de CRUD e conceitos FastAPI",
              version="1.0.0")

# -----------------------------
# Models
# -----------------------------
class Book(BaseModel):
    id: int = Field(..., example=1)
    title: str = Field(..., example="Clean Code")
    author: str = Field(..., example="Robert C. Martin")
    year: int = Field(..., ge=0, example=2008)

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

# Armazenamento em memória (simples para a tarefa)
books_db: List[Book] = []

# -----------------------------
# Dependency (exemplo simples)
# -----------------------------
async def request_timer(request: Request):
    start = time.time()
    yield
    elapsed = (time.time() - start) * 1000
    # Log simples (poderia usar logging de verdade)
    print(f"[LOG] {request.method} {request.url.path} - {elapsed:.2f}ms")

# -----------------------------
# Health Route
# -----------------------------
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}

# -----------------------------
# CRUD Routes
# -----------------------------
@app.post("/books", response_model=Book, tags=["books"], dependencies=[Depends(request_timer)])
async def create_book(book_data: BookCreate):
    new_id = (max([b.id for b in books_db]) + 1) if books_db else 1
    new_book = Book(id=new_id, **book_data.dict())
    books_db.append(new_book)
    return new_book

@app.get("/books", response_model=List[Book], tags=["books"], dependencies=[Depends(request_timer)])
async def list_books(author: Optional[str] = None):
    if author:
        return [b for b in books_db if b.author.lower() == author.lower()]
    return books_db

@app.get("/books/{book_id}", response_model=Book, tags=["books"], dependencies=[Depends(request_timer)])
async def get_book(book_id: int):
    for b in books_db:
        if b.id == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book, tags=["books"], dependencies=[Depends(request_timer)])
async def update_book(book_id: int, book_data: BookCreate):
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            updated = Book(id=b.id, **book_data.dict())
            books_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", tags=["books"], dependencies=[Depends(request_timer)])
async def delete_book(book_id: int):
    for idx, b in enumerate(books_db):
        if b.id == book_id:
            books_db.remove(b)
            return {"message": "Deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

# -----------------------------
# Custom error handler (exemplo simples)
# -----------------------------
from fastapi.responses import JSONResponse
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import RequestValidationError

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(status_code=404, content={"error": "Resource not found", "path": request.url.path})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=422, content={"error": "Validation failed", "details": exc.errors()})

# Nota: Para objetivos da tarefa, persistência não é necessária.
# Extensões possíveis: paginação, persistir em arquivo, testes automatizados.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("starter-code:app", host="0.0.0.0", port=8000, reload=True)
