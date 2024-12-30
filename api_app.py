from fastapi import FastAPI
from pydantic import BaseModel
import ollama

class IncomingPayload(BaseModel):
    text: str


app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/")
async def root(payload: IncomingPayload):
    data = payload.text
    response = ollama.chat(model='ben1t0/tiny-llm:latest', messages=[
    {
        'role': 'system',
        'content': 'you are a poet',
    },
    {
        'role': 'user',
        'content': 'limit to 50 words',
    },
    {
        'role': 'user',
        'content': data,
    },
    ])

    response['message']['content']

    return {"message":f"{payload.text}"}

@app.get("/test")
async def root():
    return {"message":"this is test"}