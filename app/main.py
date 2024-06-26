from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    #return { "Hello": "Rahti2", "v": "0.1000000" }
    return { "Hello This Is First Rahti2 APP" }


@app.get("/items/{id}")
def read_item(id: int, q: str = None):
    return {"id": id, "q": q}
