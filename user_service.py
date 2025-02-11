from fastapi import FastAPI
app = FastAPI()

@app.get("/users")
def users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("user_service:app", host="0.0.0.0", port=8000)