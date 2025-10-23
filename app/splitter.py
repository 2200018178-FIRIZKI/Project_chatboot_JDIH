
# Chunking teks: RecursiveCharacterTextSplitter

try:
	from langchain.text_splitter import RecursiveCharacterTextSplitter
except ImportError:
	from langchain.text_splitter import CharacterTextSplitter as RecursiveCharacterTextSplitter

def chunk_texts(pages, chunk_size=1000, chunk_overlap=120, keep_separator=True):
	"""
	Chunking teks hasil normalisasi per halaman.
	Args:
		pages (List[dict]): hasil normalisasi [{"page": int, "text": str}]
		chunk_size (int): ukuran chunk karakter
		chunk_overlap (int): overlap antar chunk
		keep_separator (bool): agar separator tetap utuh
	Returns:
		List[dict]: [{"page": int, "chunk_index": int, "text": str}]
	"""
	splitter = RecursiveCharacterTextSplitter(
		chunk_size=chunk_size,
		chunk_overlap=chunk_overlap,
		separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""],
		keep_separator=keep_separator
	)
	all_chunks = []
	for page in pages:
		chunks = splitter.split_text(page["text"])
		for idx, chunk in enumerate(chunks):
			all_chunks.append({
				"page": page["page"],
				"chunk_index": idx,
				"text": chunk
			})
	return all_chunks
