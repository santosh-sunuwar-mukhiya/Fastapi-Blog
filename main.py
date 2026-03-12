from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_all():
    return {"message": "Hello World"}
