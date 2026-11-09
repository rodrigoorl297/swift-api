# Swift API

reservas, catalogo e movimentacao com API versionada.

Recorte de **commerce / inventory**: estoque e pedidos divergem entre canais de venda.

## Stack

FastAPI, SQLAlchemy 2, PyJWT, Pytest, Docker.

## Setup

Copy `.env.example` to `.env` and set a real `SECRET_KEY`. Do not commit `.env`.

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
pytest -q
```

Issue a local token after the app can import settings:

```bash
python -c "from app.auth import create_token; print(create_token('local'))"
```

## Docker

```bash
docker compose up --build
```
