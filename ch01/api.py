from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello~ banga banga!",
        "name": "kkk",
        "age": 123.32
    }
