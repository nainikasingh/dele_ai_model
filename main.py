from fastapi import FastAPI
from pydantic import BaseModel
from services.qa_logic import generate_answer

app = FastAPI()

class Query(BaseModel):
    user_id: str
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = generate_answer(query.user_id, query.question)
    return {"answer": answer}
