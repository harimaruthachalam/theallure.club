from fastapi import FastAPI
from pydantic import BaseModel

class IncomingPayload(BaseModel):
    text: str


app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/")
async def root(payload: IncomingPayload):
    return {"message":f"Hello World {payload.text}"}

@app.get("/test")
async def root():
    return {"message":"this is test"}