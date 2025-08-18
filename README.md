# 🩺 Medical Encyclopedia Q&A Application

## 📌 Objective
The goal of this project is to build a **retrieval-augmented question-answering system** for medical queries, powered by **Hugging Face LLMs** and **vector search**.  
The system extracts information from a **Medical Encyclopedia PDF**, processes it into embeddings, and serves precise answers via a web interface, deployed on **AWS** using a CI/CD pipeline.

---

## 🛑 Problem Statement
Medical professionals and students often need **quick, accurate answers** from trusted medical literature.  
Traditional PDF/manual reading is slow and inefficient.

This project solves the problem by:
- Automatically processing large PDF medical references into **searchable embeddings**.
- Providing **instant, AI-generated answers** to user queries.
- Ensuring **secure deployment** and **scalability** via containerization and cloud infrastructure.

---

## 🎥 Demo & Screenshots
> Replace the placeholders below with your own demo video link and images.

### Live Demo
[![Watch the video](https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg)](https://youtu.be/VIDEO_ID)  
*(Click the thumbnail to watch on YouTube)*

### Screenshots
| Home Page | Query Example | Results Page |
|-----------|--------------|--------------|
| ![Home Page](![Xnip2025-08-18_03-16-54](https://github.com/user-attachments/assets/facd4101-28d8-4e3a-b69e-3c7439fb46e0)
) | ![Query](![Xnip2025-08-18_03-21-47](https://github.com/user-attachments/assets/a27d54a8-31c4-4b58-8aff-907158e8a4da)
  ) | ![Results](![Xnip2025-08-18_03-18-27](https://github.com/user-attachments/assets/fdc8bf6c-cf19-43d5-9c43-e2b63ab78726)
) |

---

## ⚙️ Workflow

### 1. Project & API Setup
- Create **virtual environment**.
- Implement logging & custom exceptions (production-ready).
- Define **project structure** (folders, files, `setup.py`, `requirements.txt`, `.env`).
- Generate **Hugging Face API token** & store securely in environment variables.

### 2. Data Ingestion
- Use **PyPDF** to read the medical encyclopedia PDF.
- Convert PDF content → Documents → Chunks (LangChain).

### 3. Embedding Generation
- Use Hugging Face **MiniLM-L4** embedding model to convert chunks → Embeddings.

### 4. Vector Store
- Store embeddings in **FAISS** (Facebook AI Similarity Search) local vector store.

### 5. Pipeline Integration
- Combine PDF Loader, Embedding Generator, and Vector Store into a **Data Loader** pipeline.

### 6. LLM Setup
- Use **Mistral AI** LLM via Hugging Face.
- Configure parameters (temperature, prompt format, etc.).

### 7. Retriever
- Retrieve most relevant context from the vector store based on user query.
- Pass retrieved context to LLM for final answer generation.

### 8. Frontend & Backend
- **Frontend**: HTML + CSS for user interaction.
- **Backend**: Flask handles requests, integrates with retrieval + LLM pipeline.

### 9. Containerization
- Create a **Dockerfile** defining environment, dependencies, ports, and app execution.
- Containerize the application for deployment.

### 10. Security Scanning
- Use **Aqua Trivy** to scan Docker images for vulnerabilities.
- Identify outdated packages & recommend updates.

### 11. CI/CD with Jenkins
Pipeline stages:
1. Checkout code from GitHub.
2. Build Docker image.
3. Scan image with Trivy.
4. Push image to AWS ECR (Elastic Container Registry).
5. Deploy to AWS Runner.

---

## 🌟 Key Highlights
- **LLM Integration**: Mistral AI via Hugging Face for medical Q&A.
- **Efficient Search**: FAISS vector store for fast, similarity-based retrieval.
- **Secure Deployment**: Trivy vulnerability scanning before deployment.
- **Scalable Architecture**: Docker + AWS ECR + AWS Runner.
- **Full CI/CD Pipeline**: Automated build, scan, push, and deploy with Jenkins.
- **User-Friendly UI**: HTML/CSS interface connected to Flask backend.
- **Configurable AI Behavior**: Adjustable temperature for creativity control.
- **Open Source Tools**: Fully built using free, open-source frameworks.

---

## 🛠 Tech Stack
- **LLM**: Mistral AI (Hugging Face)
- **Embeddings**: MiniLM-L4 (Hugging Face)
- **Vector Store**: FAISS (Meta)
- **Framework**: LangChain
- **PDF Processing**: PyPDF
- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Containerization**: Docker
- **Security**: Aqua Trivy
- **CI/CD**: Jenkins
- **Cloud Deployment**: AWS ECR & AWS Runner
- **SCM**: GitHub
