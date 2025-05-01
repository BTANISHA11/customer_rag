# Alltius.ai RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot designed to provide answers based on the AngelOne support documentation and insurance PDFs.

## 🧠 Features

- **Source-Based Answers**: The chatbot answers questions exclusively from the provided sources.
- **Web Scraping & PDF Ingestion**: Capable of scraping web content and ingesting PDF documents for knowledge retrieval.
- **Efficient Retrieval**: Utilizes FAISS (Facebook AI Similarity Search) for fast and efficient information retrieval.
- **Natural Language Generation**: Employs HuggingFace BART for generating human-like responses.
- **User -Friendly Interface**: Built with Streamlit for an interactive user experience.

---

## 📚 Table of Contents

- [Setup](#-setup)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Setup

Follow the steps below to set up and run the RAG chatbot:

### 1. Clone the Repository

```bash
git clone <this-repo>
cd rag_chatbot
````

### 2. Install Dependencies
### Make sure you have Python installed, then run:
       
```bash
pip install -r requirements.txt
````

### 3. Prepare Insurance PDFs
Place your insurance-related PDF documents in the docs/insurance/ directory. Ensure that the PDFs are well-structured for optimal ingestion.

### 4. Build the Index
Run the ingestion script to build the index from the provided documents:
````bash

python ingest.py
````

### 5. Launch the Chatbot
Start the Streamlit application to launch the chatbot interface:

```` bash
streamlit run app.py
````

### 📄 Usage
Once the chatbot is running, you can interact with it through the web interface. Simply type your questions related to the AngelOne support documentation or the insurance PDFs, and the chatbot will provide answers based on the ingested content.

### 🛠️ Troubleshooting
Dependencies Issues: If you encounter issues during installation, ensure that you have the correct version of Python and all required libraries.
PDF Ingestion Errors: Check the format and structure of your PDF files. They should be clear and readable for the ingestion process to work effectively.
Performance: For optimal performance, ensure your system has sufficient resources, especially if dealing with large datasets.
### 📄 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.   

### 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.   


