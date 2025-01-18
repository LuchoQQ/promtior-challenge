# server.py
from fastapi import FastAPI
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.schema import Document
import uvicorn
from dotenv import load_dotenv
from pydantic import BaseModel
import os

# Load environment variables
load_dotenv()

# Define input model
class ChatInput(BaseModel):
    input: str

# Initialize FastAPI app
app = FastAPI(
    title="Promtior Chatbot",
    version="1.0",
    description="RAG-based chatbot for Promtior website"
)

# Initialize OpenAI
embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-4")

# Manual context
MANUAL_CONTEXT = """
Promtior was founded in 2023
"""

# Load and process documents
def initialize_knowledge_base():
    # Load documents from Promtior website
    loader = WebBaseLoader("https://www.promtior.com", headers={"User-Agent": os.getenv("USER_AGENT")})
    web_docs = loader.load()
    
    # Create Document from manual context
    manual_doc = Document(page_content=MANUAL_CONTEXT)
    
    # Combine both sources
    all_docs = web_docs + [manual_doc]
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(all_docs)
    
    # Create vector store
    vector_store = FAISS.from_documents(splits, embeddings)
    retriever = vector_store.as_retriever()
    
    return retriever

# Create RAG chain
def create_rag_chain():
    retriever = initialize_knowledge_base()
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant for Promtior company. 
    Answer the question based on the following context:
    
    {context}
    
    Question: {input}
    """)
    
    # Create combining documents chain
    document_chain = create_stuff_documents_chain(llm, prompt)
    
    # Create retrieval chain
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    return retrieval_chain

# Initialize chain
chain = create_rag_chain()

# Add endpoint
@app.post("/chat/invoke")
async def chat(chat_input: ChatInput):
    response = chain.invoke({"input": chat_input.input})
    return response

# Main execution
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
