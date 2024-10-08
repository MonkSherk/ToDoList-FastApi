from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Depends, status
from .database import get_db
from .models import ToDo

# Создание задачи
async def create_todo(title: str, description: str, db: AsyncSession = Depends(get_db)) -> ToDo:
    new_todo = ToDo(title=title, description=description)
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo

# Получение списка всех задач
async def get_todos(db: AsyncSession = Depends(get_db)) -> list[ToDo]:
    query = select(ToDo)
    result = await db.execute(query)
    return result.scalars().all()

# Получение задачи по id
async def get_todo(todo_id: int, db: AsyncSession = Depends(get_db)) -> ToDo:
    result = await db.get(ToDo, todo_id)
    if result is None:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return result

# Обновление задачи
async def update_todo(todo_id: int, title: str, description: str, completed: bool, db: AsyncSession = Depends(get_db)) -> ToDo:
    todo = await get_todo(todo_id, db)
    todo.title = title
    todo.description = description
    todo.completed = completed
    await db.commit()
    await db.refresh(todo)
    return todo

# Удаление задачи
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    todo = await get_todo(todo_id, db)
    await db.delete(todo)
    await db.commit()
    return {"message": "ToDo deleted successfully"}
