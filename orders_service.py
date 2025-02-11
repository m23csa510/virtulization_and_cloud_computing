from fastapi import FastAPI, HTTPException
import requests
app = FastAPI()

@app.get("/orders")
def orders():
    try:
        users = requests.get("http://192.168.56.101:8000/users").json() # IP address of the users service. change this as per the IP address of your users service
        products = requests.get("http://192.168.56.102:8000/products").json() # IP address of the products service. change this as per the IP address of your products service
        return {"orders": [{"user_id": 1, "product_id": 1}], "users": users, "products": products}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("user_service:app", host="0.0.0.0", port=8000)