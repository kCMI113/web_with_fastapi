from fastapi import APIRouter
from model import Todo, TodoSimle

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: TodoSimle) -> dict:
    todo_list.append(todo)
    return {
        "msg": "Todo added successfully!"
    }


@todo_router.get("/todo")
async def retrive_todos() -> dict:
    return {
        "todos": todo_list
    }


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int):
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }

    return {
        "msg": "error - no id"
    }
