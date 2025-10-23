
# Loader PDF dan ekstraksi halaman
# Implementasi: pypdf, normalisasi teks
from PyPDF2 import PdfReader
from pathlib import Path

def extract_pdf_pages(pdf_path):
	"""
	Ekstrak teks per halaman dari PDF.
	Args:
		pdf_path (str or Path): path ke file PDF
	Returns:
		List[dict]: [{"page": int, "text": str}]
	"""
	pdf_path = Path(pdf_path)
	reader = PdfReader(str(pdf_path))
	pages = []
	for i, page in enumerate(reader.pages):
		text = page.extract_text() or ""
		pages.append({"page": i+1, "text": text})
	return pages


def normalize_texts(pages, header_lines=3, footer_lines=0):
	"""
	Normalisasi teks hasil ekstraksi PDF:
	- Hilangkan header/footer berulang (opsional)
	- Hilangkan whitespace berlebih
	- Perbaiki encoding karakter aneh
	Args:
		pages (List[dict]): hasil extract_pdf_pages
		header_lines (int): jumlah baris header yang dihapus (default 3)
		footer_lines (int): jumlah baris footer yang dihapus (default 0)
	Returns:
		List[dict]: hasil normalisasi
	"""
	import re
	norm_pages = []
	for page in pages:
		lines = page["text"].splitlines()
		# Hilangkan header/footer jika perlu
		if len(lines) > header_lines + footer_lines:
			lines = lines[header_lines:len(lines)-footer_lines if footer_lines > 0 else None]
		# Gabung, hilangkan whitespace berlebih
		text = " ".join([re.sub(r"\s+", " ", l.strip()) for l in lines if l.strip()])
		# Perbaiki encoding karakter aneh (contoh sederhana)
		text = text.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")
		norm_pages.append({"page": page["page"], "text": text})
	return norm_pages
