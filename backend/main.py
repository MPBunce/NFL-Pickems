from fastapi import FastAPI

app = FastAPI()

@app.get("/health-check")
async def root():
    return {"message": "Hello World Health Check"}

@app.get("/")
async def root():
    return {"message": "Healthy"}