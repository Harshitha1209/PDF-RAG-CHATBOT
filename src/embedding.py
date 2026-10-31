from langchain_huggingface import HuggingFaceEmbeddings
_embed_model = None
def get_embedding_model():
    global _embed_model

    if _embed_model is None:
        _embed_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return _embed_model