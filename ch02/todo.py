from fastapi import APIRouter, Path
from model import Todo, TodoSimple, TodoItem

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: TodoSimple) -> dict:
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
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }

    return {
        "msg": "error - no id"
    }


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "todo": "successfully"
            }

    return {
        "msg": "error - no id"
    }
