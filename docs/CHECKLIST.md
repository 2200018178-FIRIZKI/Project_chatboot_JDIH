# Checklist Implementasi RAG Chatbot PDF

| Langkah | Status |
|---|---|
| Loader PDF jalan, halaman terdeteksi benar | ❌ |
| Splitter: 800–1.000 / overlap 100–150 | ❌ |
| Embedding tersimpan ke Qdrant (collection dibuat + index OK) | ❌ |
| Metadata sinkron ke PostgreSQL | ❌ |
| Retriever: k=4 + MMR (jika ada) + threshold 0.25–0.30 | ❌ |
| Prompt 4.1/4.2 terpasang | ❌ |
| Fallback “tidak ditemukan” jika skor rendah | ❌ |
| Logging QA ke `qa_logs` (audit & tuning) | ❌ |
