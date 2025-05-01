import os
import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import fitz  # PyMuPDF
import pickle
from tqdm import tqdm

BASE_URL = "https://www.angelone.in/support"
DATA_DIR = "data/angelone_docs"
PDF_DIR = "docs/insurance"
INDEX_DIR = "vectorstore/faiss_index"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(INDEX_DIR, exist_ok=True)

# ---------- 1. Scrape AngelOne Support Pages ----------
def scrape_support_pages():
    print("Scraping AngelOne support pages...")
    urls = set([BASE_URL])

    try:
        res = requests.get(BASE_URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith("/support"):
                urls.add("https://www.angelone.in" + href)

        print(f"Found {len(urls)} support pages.")
        for url in tqdm(urls):
            try:
                res = requests.get(url)
                soup = BeautifulSoup(res.text, 'html.parser')
                text = soup.get_text()
                fname = os.path.join(DATA_DIR, url.replace('/', '_').replace(':', '') + ".txt")
                with open(fname, "w", encoding="utf-8") as f:
                    f.write(text)
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")
    except Exception as e:
        print("Failed to scrape support pages:", e)

# ---------- 2. Load PDFs ----------
def load_insurance_pdfs():
    docs = []
    print("Loading insurance PDFs...")
    for pdf_file in os.listdir(PDF_DIR):
        if pdf_file.endswith(".pdf"):
            path = os.path.join(PDF_DIR, pdf_file)
            try:
                with fitz.open(path) as doc:
                    text = ""
                    for page in doc:
                        text += page.get_text()
                    docs.append(Document(page_content=text))
            except Exception as e:
                print(f"Error reading {pdf_file}: {e}")
    return docs

# ---------- 3. Prepare Data for Embedding ----------
def get_all_documents():
    docs = []

    # Add text files
    for txt_file in os.listdir(DATA_DIR):
        with open(os.path.join(DATA_DIR, txt_file), "r", encoding="utf-8") as f:
            docs.append(Document(page_content=f.read()))

    # Add PDFs
    docs.extend(load_insurance_pdfs())
    return docs

# ---------- 4. Create FAISS Index ----------
def build_index():
    scrape_support_pages()
    raw_docs = get_all_documents()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(raw_docs)

    print("Embedding and indexing...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(INDEX_DIR)
    print("Index saved!")

if __name__ == "__main__":
    build_index()
