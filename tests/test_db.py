from app.db import save_document_metadata, save_chunk

# Uji simpan metadata dokumen
doc_id = save_document_metadata(
    title="Contoh Dokumen",
    source_path="data/2025pd0034002.pdf",
    page_count=38
)
print("doc_id:", doc_id)

# Uji simpan satu chunk
chunk_id = save_chunk(
    doc_id=doc_id,
    page=1,
    chunk_index=0,
    text="Ini adalah contoh isi chunk."
)
print("chunk_id:", chunk_id)
