from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from views import create_todo, get_todos, get_todo, update_todo, delete_todo

app = FastAPI()

@app.post("/todos/")
async def create_new_todo(title: str, description: str, db: AsyncSession = Depends(get_db)):
    return await create_todo(title=title, description=description, db=db)

@app.get("/todos/")
async def read_all_todos(db: AsyncSession = Depends(get_db)):
    return await get_todos(db=db)

@app.get("/todos/{todo_id}/")
async def read_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    return await get_todo(todo_id=todo_id, db=db)

@app.put("/todos/{todo_id}/")
async def update_existing_todo(todo_id: int, title: str, description: str, completed: bool, db: AsyncSession = Depends(get_db)):
    return await update_todo(todo_id=todo_id, title=title, description=description, completed=completed, db=db)

@app.delete("/todos/{todo_id}/")
async def delete_existing_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_todo(todo_id=todo_id, db=db)
