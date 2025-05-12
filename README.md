# 🧠 Multi-Agent Finance Assistant

## Overview
This project builds a multi-agent system that delivers a voice-interactive morning market brief.

## Architecture Diagram
```mermaid
graph TD
    A[User Voice Input] --> B[STT - Whisper]
    B --> C[Orchestrator (FastAPI)]
    C -->|query| D[API Agent]
    C -->|scrape| E[Scraping Agent]
    C -->|retrieve| F[Retriever Agent (FAISS)]
    D --> G[Data]
    E --> G
    F --> G
    G --> H[Analysis Agent]
    H --> I[Language Agent (OpenAI)]
    I --> J[Narrative Response]
    J --> K[TTS - Voice Agent]
    K --> L[User Hears Report]
    J --> M[Streamlit App]
    M --> N[User Sees Report]
```

## Agent Roles
- **API Agent**: Fetches stock data
- **Scraping Agent**: Gets earnings reports
- **Retriever Agent**: Retrieves financial document info
- **Language Agent**: Generates spoken brief
- **Voice Agent**: Converts speech to text and vice versa

## Deployment Instructions
```bash
# Step 1: Start backend
docker build -t finance-assistant .
docker run -p 8000:8000 finance-assistant

# Step 2: Run frontend
streamlit run streamlit_app/app.py
```

## Toolkit Comparison
| Function | Tool/Framework |
|---------|----------------|
| Web UI | Streamlit |
| Backend API | FastAPI |
| Financial Data | yFinance, Yahoo Finance |
| AI Model | OpenAI GPT-3.5-turbo, Whisper |
| Vector DB | FAISS + LangChain |

## Performance Benchmarks
- Retrieval latency: ~120ms (FAISS local)
- Narrative generation: ~800ms (GPT-3.5-turbo)
- TTS response: ~300ms

---