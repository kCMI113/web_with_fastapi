from pydantic import BaseModel


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: int
    item: Item


class TodoSimple(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema ~_~"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }
