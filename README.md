# Chatbot RAG PDF (LangChain, Qdrant, PostgreSQL)

Chatbot yang hanya menjawab berdasarkan PDF yang diindeks. Arsitektur modular, pipeline RAG, dan best practice untuk aplikasi hukum/umum berbasis dokumen.

## Struktur Folder

- `app/` — kode utama (pipeline, loader, retriever, rag, api)
- `data/` — PDF & data contoh
- `config/` — konfigurasi (env, db, model)
- `scripts/` — utilitas, migrasi, setup
- `tests/` — pengujian
- `docs/` — dokumentasi, prompt, checklist

## Fitur Utama
- Ingest PDF, chunk, embedding (Model-E), simpan ke Qdrant & PostgreSQL
- Retrieval top-k + MMR, threshold, fallback "tidak ditemukan"
- Prompt RAG siap pakai, logging QA
- Checklist progress implementasi

## Cara Pakai
1. Buat venv: `python3 -m venv .venv && source .venv/bin/activate`
2. Install dep: `pip install -r requirements.txt`
3. Edit config di `config/`
4. Jalankan pipeline di `app/`

## Lisensi
MIT
