import os

HF_TOKEN =os.environ.get("HF_TOKEN")

HUGGINGFACE_REPO_ID="meta-llama/Llama-3.1-8B-Instruct"
DB_FAISS_PATH="vectorstore/db_faiss"
DATA_PATH="data/"
CHUNK_SIZE=500
CHUNK_OVERLAP=50
