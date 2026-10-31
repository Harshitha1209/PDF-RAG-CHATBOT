from langchain_chroma import Chroma
import hashlib
from src.embedding import get_embedding_model

CHROMA_DIR = "./chroma_db"

def create_vector(chunks,collection_name):
    embed_model = get_embedding_model()
    vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=embed_model,
            persist_directory=CHROMA_DIR
        )

    content = "".join(chunk.page_content for chunk in chunks)
    file_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

    ids = [f"{file_hash}_{i}"
           for i in range(len(chunks))]
    # Check existing data
    existing_data = vector_store.get(ids = ids)
    existing_ids = set(existing_data["ids"])
    new_chunks = []
    new_ids = []
    for chunk,chunk_id in zip(chunks,ids):
            if chunk_id not in existing_ids:
                   new_chunks.append(chunk)
                   new_ids.append(chunk_id)
    
    if new_chunks:    
        vector_store.add_documents(
                documents=new_chunks,
                ids=new_ids
            )
    
        print("PDF chunks stored successfully.")
    
    else:
            print("PDF already exists in ChromaDB.")
    
    return vector_store
    