# Checklist Implementasi RAG Chatbot PDF

| Langkah | Status |
|---|---|
| Loader PDF jalan, halaman terdeteksi benar | ✅ |
| Splitter: 800–1.000 / overlap 100–150 | ✅ |
| Metadata dokumen & chunk tersimpan ke PostgreSQL | ✅ |
| Pengujian insert & koneksi database sukses | ✅ |
| Total chunk hasil pipeline = 66 (sudah diverifikasi) | ✅ |
| Embedding tersimpan ke Qdrant (collection dibuat + index OK) | ✅ |
| Integrasi Qdrant (vectorstore) & retrieval pipeline | ✅ |
| Retriever: k=4 + MMR (jika ada) + threshold 0.25–0.30 | ❌ |
| Prompt 4.1/4.2 terpasang | ❌ |
| Fallback “tidak ditemukan” jika skor rendah | ❌ |
| Logging QA ke `qa_logs` (audit & tuning) | ❌ |
| End-to-end RAG pipeline (retrieval → compose prompt → jawab LLM) | ❌ |
| Evaluasi & pengujian precision@k, answerable rate | ❌ |
