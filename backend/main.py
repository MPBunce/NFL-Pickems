from fastapi import FastAPI

app = FastAPI()

@app.get("/health-check", status_code=200)
async def root():
    return {"message": "Hello World Health Check"}

@app.get("/")
async def root():
    return {"message": "Healthy"}