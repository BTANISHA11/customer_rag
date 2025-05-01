from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import torch

def load_qa_chain():
    # Set device to GPU if available, otherwise CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    try:
        # Load embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
        # Load FAISS index
        db = FAISS.load_local("vectorstore/faiss_index", embeddings, allow_dangerous_deserialization=True)

        # Create retriever
        retriever = db.as_retriever(search_kwargs={"k": 4})

        # Load the text generation pipeline with proper device setting
        pipe = pipeline("text2text-generation", model="facebook/bart-base", max_length=512, device=0 if device == "cuda" else -1)
        
        # Create LLM from the pipeline
        llm = HuggingFacePipeline(pipeline=pipe)

        # Create the RetrievalQA chain
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=False
        )
        
        return qa

    except Exception as e:
        print(f"Error loading QA chain: {e}")
        return None