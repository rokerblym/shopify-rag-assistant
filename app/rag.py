import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from app.data import DOCUMENTS

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [doc["text"] for doc in DOCUMENTS]

embeddings = model.encode(texts)
embeddings = np.array(embeddings).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)


def retrieve(query: str, top_k: int = 3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for distance, idx in zip(distances[0], indices[0]):
        doc = DOCUMENTS[idx]

        results.append({
            "id": doc["id"],
            "source": doc["source"],
            "text": doc["text"],
            "score": float(distance)
        })

    return results