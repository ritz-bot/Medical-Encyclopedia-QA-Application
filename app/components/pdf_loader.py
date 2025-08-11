'''import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data path doesn't exist")
        
        logger.info(f"loading files from {DATA_PATH}")
        loader=DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)

        documents=loader.load()

        if not documents:
            logger.warning("no pdfs were found")
        else:
            logger.info(f"Succesfully fetched {len(documents)} documents")


        return documents
    
    except Exception as e:
        error_message=CustomException("Failed to load PDF", e)
        logger.error(str(error_message))
        return[]
    

def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents were found")
        
        logger.info(f"Splitting {len(documents)} documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)

        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks
    
    except Exception as e:
        error_message = CustomException("Failed to generate chunks" , e)
        logger.error(str(error_message))
        return []

'''

import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_pdf_files():
    print(f"Configured DATA_PATH: {DATA_PATH}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Configured DATA_PATH: {DATA_PATH}")
    print(f"Absolute DATA_PATH: {os.path.abspath(DATA_PATH)}")
    print(f"Does DATA_PATH exist? {os.path.exists(DATA_PATH)}")
    try:
        if not os.path.exists(DATA_PATH):
            print("DATA_PATH does not exist according to Python, raising exception.")
            raise CustomException("Data path doesn't exist")
        
        logger.info(f"loading files from {DATA_PATH}")

        abs_pdf_dir = os.path.abspath(DATA_PATH)
        print(f"PDF directory being used: {abs_pdf_dir}")
        
        pdf_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".pdf")] if os.path.exists(DATA_PATH) else []
        print(f"PDF files found: {pdf_files}")
        if not pdf_files:
            print("Warning: No PDF files in directory. Check if the path is correct and files exist.")
        
        loader=DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)

        documents=loader.load()

        print(f"Number of documents loaded: {len(documents)}")
        if documents:
            print(f"Sample document content (first 100 chars): {documents[0].page_content[:100]}")

        if not documents:
            logger.warning("no pdfs were found")
        else:
            logger.info(f"Succesfully fetched {len(documents)} documents")


        return documents
    
    except Exception as e:
        error_message=CustomException("Failed to load PDF", e)
        logger.error(str(error_message))
        return[]
    

def create_text_chunks(documents):
    try:
        print(f"Number of input documents for chunking: {len(documents)}")
        if not documents:
            print("Warning: No documents to chunk.")
        
        if not documents:
            raise CustomException("No documents were found")
        
        logger.info(f"Splitting {len(documents)} documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)

        text_chunks = text_splitter.split_documents(documents)

        print(f"Number of chunks created: {len(text_chunks)}")
        if text_chunks:
            print(f"Sample chunk (first 100 chars): {text_chunks[0].page_content[:100]}")

        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks
    
    except Exception as e:
        error_message = CustomException("Failed to generate chunks" , e)
        logger.error(str(error_message))
        return []






