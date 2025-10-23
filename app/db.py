import hashlib
def save_chunk(doc_id, page, chunk_index, text):
	"""
	Simpan satu chunk ke tabel chunks.
	Args:
		doc_id (str): UUID dokumen
		page (int): nomor halaman
		chunk_index (int): index chunk di halaman
		text (str): isi chunk
	Returns:
		chunk_id (UUID)
	"""
	chunk_id = str(uuid.uuid4())
	text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
	created_at = datetime.now()
	conn = get_pg_conn()
	cur = conn.cursor()
	cur.execute(
		"""
		INSERT INTO chunks (chunk_id, doc_id, page, chunk_index, text, text_hash, created_at)
		VALUES (%s, %s, %s, %s, %s, %s, %s)
		""",
		(chunk_id, doc_id, page, chunk_index, text, text_hash, created_at)
	)
	conn.commit()
	cur.close()
	conn.close()
	return chunk_id

# Koneksi & sinkronisasi PostgreSQL
import psycopg2
import uuid
from datetime import datetime

def get_pg_conn():
	# Konfigurasi bisa diambil dari config.yaml atau .env
	return psycopg2.connect(
		dbname="ragdb",
		user="postgres",
		password="Madinah017#",
		host="localhost",
		port=5432
	)

def save_document_metadata(title, source_path, page_count):
	"""
	Simpan metadata dokumen ke tabel documents.
	Args:
		title (str): judul dokumen
		source_path (str): path file sumber
		page_count (int): jumlah halaman
	Returns:
		doc_id (UUID)
	"""
	doc_id = str(uuid.uuid4())
	created_at = datetime.now()
	conn = get_pg_conn()
	cur = conn.cursor()
	cur.execute(
		"""
		INSERT INTO documents (doc_id, title, source_path, page_count, created_at)
		VALUES (%s, %s, %s, %s, %s)
		""",
		(doc_id, title, source_path, page_count, created_at)
	)
	conn.commit()
	cur.close()
	conn.close()
	return doc_id
