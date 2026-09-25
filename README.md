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
## Why I Built This

I built this project to practice the same core ideas used in AI support systems: semantic retrieval, grounded answers, source citations, and backend API design.

The goal was to create a small but working prototype similar to the kind of product flow used in AI concierge and e-commerce support systems.