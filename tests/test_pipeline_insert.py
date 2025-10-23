from app.loader import extract_pdf_pages, normalize_texts
from app.splitter import chunk_texts
from app.db import save_document_metadata, save_chunk

PDF_PATH = "data/2025pd0034002.pdf"

def main():
    # 1. Ekstrak teks per halaman
    pages = extract_pdf_pages(PDF_PATH)
    print(f"Extracted {len(pages)} pages")

    # 2. Normalisasi teks
    norm_pages = normalize_texts(pages)
    print(f"Normalized {len(norm_pages)} pages")

    # 3. Chunking
    chunks = chunk_texts(norm_pages)
    print(f"Generated {len(chunks)} chunks")

    # 4. Simpan metadata dokumen
    doc_id = save_document_metadata(
        title="Dokumen PDF Uji Coba",
        source_path=PDF_PATH,
        page_count=len(pages)
    )
    print(f"Saved document metadata, doc_id: {doc_id}")

    # 5. Simpan semua chunk ke database
    for chunk in chunks:
        chunk_id = save_chunk(
            doc_id=doc_id,
            page=chunk["page"],
            chunk_index=chunk["chunk_index"],
            text=chunk["text"]
        )
        print(f"Saved chunk: {chunk_id}")

if __name__ == "__main__":
    main()
