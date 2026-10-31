
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(pdf_path):

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print("\n ----- PDF EXTRACTION TEST ------")
    for doc in documents[:3]:
        print("\nPage:",doc.metadata.get("page",0) + 1)
        print(doc.page_content[:1000])

    print("\n ----")
    if not documents:
        raise ValueError("No text extracted from PDF.")

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    if not chunks:
        raise ValueError("No text chunks created.")
    print("PDF pages:",len(documents))
    print("Chunks created:",len(chunks))
    return chunks