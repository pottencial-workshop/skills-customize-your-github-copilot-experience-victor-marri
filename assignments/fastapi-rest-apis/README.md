# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective
Construir uma API REST simples utilizando o framework FastAPI, praticando criação de rotas, modelos de dados com Pydantic, operações CRUD, validação, documentação automática e boas práticas de organização.

## 🧠 Learning Goals
Ao final desta tarefa, você deverá ser capaz de:
- Criar um projeto básico FastAPI e executá-lo com Uvicorn
- Definir modelos de dados com Pydantic e utilizá-los em rotas
- Implementar operações CRUD em um recurso simples (ex.: livros)
- Tratar erros e retornar respostas HTTP adequadas
- Usar recursos de documentação automática (OpenAPI/Swagger UI)
- Aplicar filtros simples usando query parameters

## 📝 Tasks

### 🛠️ 1. Configuração do Projeto e Rota Inicial

#### Description
Configurar o ambiente, instalar dependências e criar um primeiro endpoint de saúde da aplicação.

#### Requirements
Completed program should:
- Ter um arquivo `starter-code.py` (ou renomeado para `main.py`) executável via Uvicorn
- Incluir rota `GET /health` retornando JSON: `{ "status": "ok" }`
- Exibir a documentação automática em `/docs`
- Usar estrutura mínima clara e comentada

### 🛠️ 2. Implementar CRUD para Recurso "Book"

#### Description
Criar um conjunto de rotas para manipular uma coleção de livros em memória.

#### Requirements
Completed program should:
- Definir modelo `Book` com campos: `id: int`, `title: str`, `author: str`, `year: int`
- Implementar endpoints:
  - `POST /books` (criar)
  - `GET /books` (listar todos)
  - `GET /books/{book_id}` (obter por id)
  - `PUT /books/{book_id}` (atualizar)
  - `DELETE /books/{book_id}` (remover)
- Armazenar dados numa lista em memória (não precisa de banco)
- Retornar 404 para IDs inexistentes
- Garantir validação automática via Pydantic

### 🛠️ 3. Melhorias, Filtros e Boas Práticas

#### Description
Adicionar funcionalidades adicionais para melhorar a usabilidade e a manutenção do código.

#### Requirements
Completed program should:
- Adicionar filtro opcional em `GET /books` por autor: `GET /books?author=Nome`
- Usar `response_model` para tipar respostas nas rotas principais
- Adicionar exemplos (`Config` ou `Field(example=...)`) ao modelo
- Criar um handler simples de erro para 404 customizado com mensagem clara
- Adicionar uma dependência simples que registra tempo de processamento ou log básico
- Incluir docstring ou comentário explicando cada parte principal

## ✅ Entrega
Você deve entregar:
- Arquivo de código com a API funcional
- Rotas testáveis via Swagger UI (acesso em `/docs`)
- Código organizado e legível

## 🧪 Sugestões de Teste Manual
- Criar dois livros e verificar se aparecem na listagem
- Buscar um livro por ID existente e um inexistente (deve retornar 404)
- Atualizar título de um livro e conferir alteração
- Filtrar por autor usando query param
- Remover um livro e garantir que desaparece da listagem

## 🚀 Extensões (Opcional)
- Paginação simples (`?skip=0&limit=10`)
- Persistência em arquivo JSON
- Testes automatizados com `pytest`

## ▶️ Como Executar (Sugestão)
```
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```
Abra: http://127.0.0.1:8000/docs

Boa prática: após terminar, refatore para separar modelos, rotas e dependências (não obrigatório nesta entrega inicial).
