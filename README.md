# RAG Chatbot

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) chatbot built using Python. It enables users to query enterprise documents using natural language by combining document retrieval with Large Language Models (LLMs).

The application processes PDF and CSV files, creates vector embeddings, and retrieves relevant information to generate accurate responses based on the uploaded documents.

---

## Features

- Process PDF documents
- Process CSV files
- Create vector embeddings
- Build searchable vector indexes
- Natural language question answering
- Modular Python implementation
- Easy to extend with additional document types

---

## Architecture

```
                PDF / CSV Files
                      │
                      ▼
            Document Processing
                      │
                      ▼
              Text Chunking
                      │
                      ▼
            Vector Embeddings
                      │
                      ▼
             Vector Database
                      │
                      ▼
        Large Language Model (LLM)
                      │
                      ▼
              Chatbot Response
```

---

## Tech Stack

- Python
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- PDF Processing
- CSV Processing

---

## Project Structure

```
RAG-Chatbot
│
├── create_tables.py
├── pdf_loader.py
├── csv_loader.py
├── vector_index.py
├── chatbot.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

1. Load PDF or CSV documents.
2. Extract and preprocess text.
3. Generate vector embeddings.
4. Store embeddings in a vector database.
5. Retrieve relevant document chunks.
6. Generate responses using an LLM.

---

## Use Cases

- Enterprise knowledge search
- Internal document assistant
- Policy and compliance search
- Technical documentation chatbot
- Customer support knowledge base

---

## Future Enhancements

- Multi-document support
- Conversation history
- User authentication
- Streamlit web interface
- Azure OpenAI integration
- AWS deployment
- Docker support

---

## Author

**Santhosh T**

Senior Data Engineer

GitHub:
https://github.com/10631A1236
