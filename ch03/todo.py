from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
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

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "todo": "successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.delete("/todo/{todo_id}")
async def delete_all_todo(todo_id: int) -> dict:
    for idx in range(len(todo_list)):
        todo = todo_list[idx]
        if todo_id == todo.id:
            todo_list.pop(idx)
            return {
                "msg": "Todo deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist"
    )


@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }
