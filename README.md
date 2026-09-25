# Shopify RAG Support Assistant

A lightweight RAG-style support assistant built with Python and FastAPI.

The project retrieves the most relevant information from a small Shopify-style knowledge base and returns grounded answers with source citations and confidence scores.

## Features

- Semantic retrieval
- Grounded answers
- Source citations
- Confidence scoring
- REST API with FastAPI
- JSON responses
- Swagger documentation

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- FAISS
- Pydantic
- REST API

## Example Request

POST `/ask`

```json
{
  "question": "How long does shipping take?"
}
```

## Example Response

```json
{
  "question": "How long does shipping take?",
  "answer": "Orders are processed within 1 to 2 business days. Standard shipping takes 3 to 5 business days.",
  "confidence": "high",
  "sources": [
    {
      "source": "Shipping Policy",
      "text": "Orders are processed within 1 to 2 business days. Standard shipping takes 3 to 5 business days."
    }
  ]
}
```

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

## Why I Built This

I built this project to practice the same core ideas used in AI support systems: semantic retrieval, grounded answers, source citations, and backend API design.

The goal was to create a small but working prototype similar to the kind of product flow used in AI concierge and e-commerce support systems.