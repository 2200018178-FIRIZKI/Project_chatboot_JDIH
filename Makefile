
# Makefile untuk pipeline RAG PDF
#
# Urutan langkah development:
# 1. Pastikan PostgreSQL sudah berjalan (service postgresql start)
# 2. Buat dan aktifkan venv: make venv
# 3. Install requirements: make install
# 4. Migrasi DB (jika ada): make migrate
# 5. Jalankan Qdrant: make qdrant-up
# 6. Jalankan pipeline embedding: make embedding
# 7. Jalankan aplikasi utama: make run
# 8. Jalankan test: make test
# 9. Linting: make lint
# 10. Stop Qdrant: make qdrant-down
# 11. Bersihkan environment: make clean


venv:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

install:
	pip install -r requirements.txt

run:
	. venv/bin/activate && python app/main.py

test:
	. venv/bin/activate && pytest tests/

lint:
	. venv/bin/activate && flake8 app/ tests/

migrate:
	. venv/bin/activate && python scripts/migrate.py

embedding:
	. venv/bin/activate && PYTHONPATH=. python app/embedding.py

qdrant-up:
	docker start qdrant || docker run --name qdrant -p 6333:6333 -p 6334:6334 qdrant/qdrant

qdrant-down:
	docker stop qdrant

clean:
	rm -rf venv __pycache__ *.pyc .mypy_cache .pytest_cache
