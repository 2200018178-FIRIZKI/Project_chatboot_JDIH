
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import psycopg2

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Koneksi ke Qdrant
qdrant = QdrantClient("localhost", port=6333)
COLLECTION_NAME = "laws"

# Koneksi ke PostgreSQL
conn = psycopg2.connect(
	dbname="ragdb",
	user="postgres",
	password="Madinah017#",
	host="localhost",
	port=5432
)
cur = conn.cursor()
cur.execute("SELECT chunk_id, doc_id, page, chunk_index, text FROM chunks")
rows = cur.fetchall() #list of tuples

# Buat collection jika belum ada
collections = qdrant.get_collections().collections
if COLLECTION_NAME not in [c.name for c in collections]:
	qdrant.create_collection(
		collection_name=COLLECTION_NAME,
		vectors_config={"size": 384, "distance": "Cosine"}
	)

# Embedding dan insert ke Qdrant
for chunk_id, doc_id, page, chunk_index, text in rows:
	vector = model.encode(text).tolist()
	payload = {
		"doc_id": str(doc_id),
		"page": page,
		"chunk_index": chunk_index,
		"text": text
	}
	qdrant.upsert(
		collection_name=COLLECTION_NAME,
		points=[{
			"id": str(chunk_id),
			"vector": vector,
			"payload": payload
		}]
	)

cur.close()
conn.close()
print("Embedding dan insert ke Qdrant selesai.")
