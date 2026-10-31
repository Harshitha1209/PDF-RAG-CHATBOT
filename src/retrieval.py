from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from src.embedding import get_embedding_model

CHROMA_DIR = "./chroma_db"

_llm = None

def get_llm():
    global _llm

    if _llm is None:
        _llm = ChatOllama(
            model="llama3.2:3b",
            temperature=0
        )

    return _llm

def format_docs(docs):

    formatted_docs = []

    for doc in docs:

        page = doc.metadata.get("page", "unknown")

        if isinstance(page, int):
            page += 1

        formatted_docs.append(
            f"Page {page}:\n{doc.page_content}"
        )

    return "\n\n".join(formatted_docs)



prompt = ChatPromptTemplate.from_template("""
You are a helpful educational assistant.

Answer the user's question using the provided context.

Instructions:
1. Read all the context carefully.
2. Identify the relevant information.
3. Give a clear and simple explanation.
4. You may combine information from multiple passages.
5. Do not say "I don't know" if the answer
   is available in the context.
6. Do not invent information that is not supported
   by the context.

Context:
{context}

Question:
{question}

Answer:
""")


# Ask question
def ask_question(question, collection_name):

    # Connect to the correct PDF collection
    vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=get_embedding_model(),
        persist_directory=CHROMA_DIR
    )

    # Create retriever
    results = vector_store.similarity_search_with_score(
        question, k=5
    )

    if not results:
        return "No relevant information found in the PDF.", []

    docs = [doc for doc, score in results]

    print("\n========== RETRIEVED DOCUMENTS ==========")

    for i, (doc, score) in enumerate(results, 1):
    
        print(f"\nChunk {i}")
        print("Page:", doc.metadata.get("page", "unknown") + 1)
        print("Similarity distance:", score)
        print("Content:", doc.page_content)

    print("\n=========================================")

    # Prepare context
    context = format_docs(docs)

    # Build RAG chain
    rag_chain = (
        prompt
        | get_llm()
        | StrOutputParser()
    )

    # Generate answer
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })

    # Extract source pages
    sources = sorted({
        doc.metadata.get("page", 0) + 1
        for doc in docs
        if isinstance(doc.metadata.get("page"), int)
    })

    return answer, sources
