from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
async def root():
    return {"message": "Hello World Health Check"}

@app.get("/")
async def root():
    return {"message": "Healthy"}