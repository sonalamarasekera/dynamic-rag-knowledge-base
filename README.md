# NAIVE-RAG Chatbot (HuggingFace Embeddings + FAISS + Ollama)

This is a **Retrieval Augmented Generation (RAG) chatbot** that can handle pdfs and docx files. Users are able to ask questions from documents uploaded to the specified folder (data).

It is built using **Langchain**, **HuggingFace Embeddings**, **FAISS**, **Ollama** and then **Streamlit** for the UI.

---

## Setting Up
### 1. Create a virtual environment
```bash
# Creating virtual environment
python -m venv venv

# Activate the environment
# --- Windows ---
venv/Scripts/activate
# --- MacOS/Linux ---
source venv/bin/activate
```
### 2. Install dependencies
```bash
# Clone the repository
git clone https://github.com/sonalamarasekera/nexus-rag-chatbot.git

# After moving into the cloned repo, install dependencies
pip install -r requirements.txt

# Also install the additional package below
# --- Windows ---
winget install zstd
# --- MacOS ---
brew install zstd
# --- Linux ---
sudo apt-get install zstd
```
### 3. Download Ollama and preferred model

Download from: https://ollama.com/download or
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
### 4. Build the FAISS index
### 5. Run UI

---

## Features