# 📚 PDF RAG Chatbot | Document Question Answering System

An interactive PDF Question Answering Chatbot built using **Retrieval-Augmented Generation (RAG)**, LangChain, HuggingFace Embeddings, ChromaDB, Ollama, and Streamlit.

## 🚀 Project Overview

The PDF RAG Chatbot allows users to upload PDF documents and ask questions based on their content.

It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded PDF documents and generate context-based answers using a locally running Large Language Model (LLM).

Instead of relying only on the LLM's pre-trained knowledge, the system retrieves relevant document chunks and uses them as context to generate answers.

## ✨ Key Features

- 📄 Upload PDF documents through an interactive Streamlit interface.
- ✂️ Extract text and split documents into smaller chunks.
- 🔢 Generate vector embeddings using HuggingFace Sentence Transformers.
- 🗄️ Store document embeddings in ChromaDB.
- 🔍 Retrieve relevant document chunks using similarity search.
- 🤖 Generate context-based answers using Ollama and Llama 3.2.
- 📖 Display source page numbers for retrieved information.
- 🔒 Run the LLM locally using Ollama.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Frontend application |
| LangChain | RAG pipeline development |
| PyPDFLoader | PDF document loading |
| RecursiveCharacterTextSplitter | Text chunking |
| HuggingFace Embeddings | Text vectorization |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Vector database |
| Ollama | Local LLM execution |
| Llama 3.2 (3B) | Answer generation |

## 🏗️ RAG Architecture

The application follows this workflow:

1. **PDF Upload:** User uploads a PDF document.
2. **Document Loading:** PyPDFLoader extracts text from the PDF.
3. **Text Splitting:** RecursiveCharacterTextSplitter divides the extracted text into chunks.
4. **Embedding Generation:** HuggingFace converts text chunks into numerical vector representations.
5. **Vector Storage:** ChromaDB stores the embeddings and associated document chunks.
6. **User Query:** User enters a question through the Streamlit interface.
7. **Similarity Search:** ChromaDB retrieves the top 5 relevant document chunks.
8. **Context Preparation:** Retrieved chunks are formatted and passed to the LLM.
9. **Answer Generation:** Ollama runs Llama 3.2 to generate an answer using the retrieved context.
10. **Response Display:** Streamlit displays the generated answer and source page numbers.

## 📂 Project Structure

```text
PDF-RAG-Practice/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retrieval.py
│   └── rag_pipeline.py
│
└── chroma_db/
```

### Module Description

- **app.py:** Streamlit user interface for PDF uploading and question answering.
- **preprocess.py:** Loads PDF documents and performs text chunking.
- **embedding.py:** Generates text embeddings using HuggingFace.
- **vector_store.py:** Creates and manages the ChromaDB vector store.
- **retrieval.py:** Performs similarity search and generates answers using the LLM.
- **rag_pipeline.py:** Integrates preprocessing and vector storage into the PDF processing pipeline.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PDF-RAG-Chatbot.git

cd PDF-RAG-Chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install and Configure Ollama

Download Ollama:

https://ollama.com/

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2:3b
```

Ensure Ollama is running locally before starting the application.

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 💬 How to Use

1. Open the PDF RAG Chatbot application.
2. Upload your PDF document.
3. Click the **Process PDF** button.
4. Wait until document processing and embedding generation are completed.
5. Enter your question in the chat interface.
6. Receive an AI-generated answer based on the document.
7. View the source pages used for the answer.

## 🧠 Retrieval-Augmented Generation (RAG)

This project implements a basic RAG architecture consisting of two major stages:

**1. Retrieval**

Relevant document chunks are retrieved from ChromaDB using vector similarity search.

**2. Generation**

The retrieved context and user question are passed to Llama 3.2 through Ollama to generate a context-based response.

## 🔮 Future Enhancements

- Multiple PDF document support.
- Conversation history and memory.
- Hybrid search techniques.
- Retrieval evaluation and optimization.
- Reranking for improved retrieval accuracy.
- Improved document processing for scanned PDFs.
- Cloud deployment.

## 👩‍💻 Author

**Harshitha**

AI/ML | Generative AI | Python | RAG

---

⭐ If you find this project useful, consider giving the repository a star!
