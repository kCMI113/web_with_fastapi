from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": "Read next"
        }


class TodoItems(BaseModel):
    todo: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "ex1"},
                    {"item": "ex2"}
                ]
            }
        }
