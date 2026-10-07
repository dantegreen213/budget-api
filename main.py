from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    amount: float
    category: str

engine = create_engine("sqlite:///budget.db")
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.post("/expenses")
def add_expense(expense: Expense):
    with Session(engine) as s:
        s.add(expense)
        s.commit()
        s.refresh(expense)
        return expense

@app.get("/expenses")
def list_expenses():
    with Session(engine) as s:
        return s.exec(select(Expense)).all()

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    with Session(engine) as s:
        expense = s.get(Expense, expense_id)
        if not expense:
            raise HTTPException(status_code=404, detail="Not found")
        s.delete(expense)
        s.commit()
        return {"deleted": expense_id}
