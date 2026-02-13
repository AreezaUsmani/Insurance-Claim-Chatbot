from flask import Flask, render_template, request, jsonify
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os

app = Flask(__name__)

PDF_PATH = "insurance_policy.pdf"
DB_DIR = "chroma_db"

# ---------- SETUP ----------
def setup_vectorstore():
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    docs = splitter.split_documents(pages)

    embeddings = OllamaEmbeddings(model="llama3.2")

    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    return vectordb

vectorstore = setup_vectorstore()

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "")

    if not question:
        return jsonify({"response": "Please ask a question."})

    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an insurance assistant.
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return jsonify({"response": response.content})

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)

