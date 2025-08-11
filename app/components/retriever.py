'''from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store

from app.config.config import HUGGINGFACE_REPO_ID,HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE,input_variables=["context" , "question"])

def create_qa_chain():
    try:
        logger.info("Loading vector store for context")
        db = load_vector_store()

        if db is None:
            raise CustomException("Vector store not present or empty")

        llm = load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID , hf_token=HF_TOKEN )

        if llm is None:
            raise CustomException("LLM not loaded")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever = db.as_retriever(search_kwargs={'k':3}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': set_custom_prompt()}
        )

        logger.info("Sucesfully created the QA chain")
        return qa_chain
    
    except Exception as e:
        error_message = CustomException("Failed to make a QA chain", e)
        logger.error(str(error_message))
        raise error_message
        '''
'''
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint  # Added import for direct LLM init

from app.components.vector_store import load_vector_store

from app.config.config import HUGGINGFACE_REPO_ID,HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE,input_variables=["context" , "question"])

def create_qa_chain():
    try:
        logger.info("Loading vector store for context")
        db = load_vector_store()

        if db is None:
            raise CustomException("Vector store not present or empty")

        # Replaced load_llm with direct init to include task parameter for provider compatibility
        llm = HuggingFaceEndpoint(
            repo_id=HUGGINGFACE_REPO_ID,
            huggingfacehub_api_token=HF_TOKEN,
            task="conversational", # Added to fix task/provider mismatch; use "text-generation" if supported for your model
            endpoint_url="https://api.fireworks.ai/inference/v1/chat/completions"  # Force conversational endpoint
        )
        print(f"LLM initialized with repo: {HUGGINGFACE_REPO_ID} and task: {llm.task}")  # Add this to confir
        print(f"DEBUG: LLM repo_id loaded as: {HUGGINGFACE_REPO_ID}")
        print(f"DEBUG: LLM task set to: {llm.task}")

        if llm is None:
            raise CustomException("LLM not loaded")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever = db.as_retriever(search_kwargs={'k':3}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': set_custom_prompt()}
        )

        logger.info("Sucesfully created the QA chain")
        return qa_chain
    
    except Exception as e:
        error_message = CustomException("Failed to make a QA chain", e)
        logger.error(str(error_message))
        raise error_message

        '''
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace  # Added ChatHuggingFace

from app.components.vector_store import load_vector_store

from app.config.config import HUGGINGFACE_REPO_ID,HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException


logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE,input_variables=["context" , "question"])

def create_qa_chain():
    try:
        logger.info("Loading vector store for context")
        db = load_vector_store()

        if db is None:
            raise CustomException("Vector store not present or empty")

        # Create base LLM endpoint
        base_llm = HuggingFaceEndpoint(
            repo_id=HUGGINGFACE_REPO_ID,
            huggingfacehub_api_token=HF_TOKEN,
        )

        # Wrap with ChatHuggingFace to use conversational task
        llm = ChatHuggingFace(llm=base_llm)

        if llm is None:
            raise CustomException("LLM not loaded")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever = db.as_retriever(search_kwargs={'k':3}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': set_custom_prompt()}
        )

        logger.info("Sucesfully created the QA chain")
        return qa_chain
    
    except Exception as e:
        error_message = CustomException("Failed to make a QA chain", e)
        logger.error(str(error_message))
        raise error_message