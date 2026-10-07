# Budget API

A REST API for tracking expenses, built with FastAPI, SQLModel and SQLite.

## Run it
    uv run uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs

## Endpoints
- POST /expenses: add an expense
- GET /expenses: list all expenses
- DELETE /expenses/{id}: delete an expense
