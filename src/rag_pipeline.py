import hashlib
from src.vector_store import create_vector
from src.preprocess import load_pdf

def process_pdf(pdf_path):
    with open(pdf_path,"rb") as file:
        file_hash = hashlib.sha256(file.read()).hexdigest()
    collection_name = f"pdf_{file_hash[:20]}"

    chunks = load_pdf(pdf_path)

    vector_store = create_vector(
        chunks,
        collection_name
    )

    return len(chunks),collection_name