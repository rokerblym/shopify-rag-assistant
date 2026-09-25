from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import retrieve

app = FastAPI(
    title="Shopify RAG Support Assistant",
    description="Grounded support assistant with retrieval and source citations"
)


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Shopify RAG Support Assistant"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):
    results = retrieve(request.question, top_k=3)

    if not results:
        return {
            "question": request.question,
            "answer": "I could not find enough information in the knowledge base.",
            "confidence": "low",
            "sources": []
        }

    best = results[0]

    # Lower FAISS L2 distance = more relevant
    if best["score"] < 0.8:
        confidence = "high"
    elif best["score"] < 1.2:
        confidence = "medium"
    else:
        confidence = "low"

    return {
        "question": request.question,
        "answer": best["text"],
        "confidence": confidence,
        "sources": [
            {
                "source": item["source"],
                "text": item["text"],
                "score": round(item["score"], 4)
            }
            for item in results
        ]
    }