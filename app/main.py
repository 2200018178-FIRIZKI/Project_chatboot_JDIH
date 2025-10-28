# Entry point aplikasi RAG Chatbot PDF


from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

def main():
    print("RAG Chatbot PDF — pipeline sederhana")
    # 1. Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # 2. Koneksi ke Qdrant
    qdrant = QdrantClient("localhost", port=6333)
    collection = "laws"

    # 3. Input query
    query = input("Masukkan pertanyaan: ")
    query_vec = model.encode(query).tolist()

    # 4. Retrieve top-4 chunk dari Qdrant
    result = qdrant.search(
        collection_name=collection,
        query_vector=query_vec,
        limit=4
    )
    print("\nHasil retrieval:")
    for i, point in enumerate(result):
        print(f"[{i+1}] Skor: {point.score:.3f}")
        print(f"Halaman: {point.payload.get('page')}, Chunk: {point.payload.get('chunk_index')}")
        print(f"Teks: {point.payload.get('text')[:200]} ...\n")

if __name__ == "__main__":
    main()
