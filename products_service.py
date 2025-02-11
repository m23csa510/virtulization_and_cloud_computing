from fastapi import FastAPI
app = FastAPI()

@app.get("/products")
def products():
    return [{"id": 1, "name": "Book"}, {"id": 2, "name": "Laptop"}]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("user_service:app", host="0.0.0.0", port=8000)