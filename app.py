
import streamlit as st
import tempfile
import os

from src.rag_pipeline import process_pdf
from src.retrieval import ask_question


# Page configuration
st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📚",
    layout="wide"
)


# Initialize session state
if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

if "collection_name" not in st.session_state:
    st.session_state.collection_name = None

if "pdf_name" not in st.session_state:
    st.session_state.pdf_name = None

if "messages" not in st.session_state:
    st.session_state.messages = []


# Main title
st.title("📚 PDF RAG Chatbot")

st.write(
    "Upload your PDF and ask questions based on its content."
)


# Sidebar
with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose your PDF file",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.write(f"Selected: {uploaded_file.name}")

        if st.button("Process PDF", use_container_width=True):

            temp_path = None

            try:

                with st.spinner(
                    "Loading PDF, creating chunks and embeddings..."
                ):

                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=".pdf"
                    ) as temp:

                        temp.write(uploaded_file.getvalue())
                        temp_path = temp.name

                    chunks, collection_name = process_pdf(temp_path)

                    st.session_state.pdf_processed = True
                    st.session_state.collection_name = collection_name
                    st.session_state.pdf_name = uploaded_file.name
                    st.session_state.messages = []

                st.success(
                    f"PDF processed successfully! {chunks} chunks created."
                )

            except Exception as e:

                st.error("Error while processing PDF.")
                st.exception(e)

            finally:

                if temp_path and os.path.exists(temp_path):
                    os.remove(temp_path)

    st.divider()

    if st.session_state.pdf_processed:

        st.success(
            f"Active PDF: {st.session_state.pdf_name}"
        )

    if st.button("Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.rerun()


# Main chat section
if not st.session_state.pdf_processed:

    st.info(
        "👈 Upload and process a PDF from the sidebar to start chatting."
    )

else:

    st.subheader("💬 Chat with your PDF")

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

            if message["role"] == "assistant":
                st.caption(
                    "Source pages: " +
                    ", ".join(map(str, message["sources"]))
                )

    # User question
    question = st.chat_input(
        "Ask a question about your PDF..."
    )

    if question:

        # Display user message
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        # Generate answer
        with st.chat_message("assistant"):

            try:

                with st.spinner("Generating answer..."):

                    answer, sources = ask_question(
                        question,
                        st.session_state.collection_name
                    )

                st.markdown(answer)

                st.caption(
                    "Source pages: " +
                    ", ".join(map(str, sources))
                )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as e:

                st.error("Unable to generate the answer.")
                st.exception(e)
