# Urutan Sintaks Manual Pipeline RAG Chatbot PDF

## 1. Pastikan PostgreSQL dan Qdrant sudah berjalan
sudo service postgresql start

docker start qdrant || docker run --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant

---
## 2. Buat dan aktifkan virtual environment
python3 -m venv venv
source venv/bin/activate

---
## 3. Install semua dependencies
pip install -r requirements.txt

---
## 4. Migrasi database (jika ada perubahan skema)
PYTHONPATH=. python3 scripts/migrate.py

---
## 5. Jalankan pipeline loader, splitter, dan simpan ke DB
PYTHONPATH=. python3 app/loader.py
PYTHONPATH=. python3 app/splitter.py
PYTHONPATH=. python3 app/db.py

---
## 6. Jalankan pipeline embedding (simpan vektor ke Qdrant)
PYTHONPATH=. python3 app/embedding.py

---
## 7. Jalankan aplikasi utama (chatbot retrieval)
PYTHONPATH=. python3 app/main.py

---
## 8. Jalankan test (opsional)
PYTHONPATH=. python3 -m pytest tests/

---
## 9. Linting (opsional)
PYTHONPATH=. python3 -m flake8 app/ tests/

---
## 10. Stop Qdrant (opsional)
docker stop qdrant

---
## 11. Bersihkan environment (opsional)
rm -rf venv __pycache__ *.pyc .mypy_cache .pytest_cache

## 12. http://localhost:6333/dashboard