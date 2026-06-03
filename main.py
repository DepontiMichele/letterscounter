from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextPayload(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "running"}

@app.post("/count")
def count_words(payload: TextPayload):
    words = payload.text.split()
    return {"word_count": len(words)}
