from typing import List, Optional
from pydantic import BaseModel
from fastapi import Form


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)


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
