## AI Tool Usage
- **OpenAI GPT**: Used for narrative generation with `gpt-3.5-turbo` model
- **Whisper**: Used for speech-to-text transcription (model: `base`)
- **LangChain + FAISS**: Used for semantic document retrieval

### Prompt Logs & Code Generation
- Prompt to GPT: `Create a brief summary: {market and earnings data}`
- Whisper model used: `base`
- FAISS used with OpenAIEmbeddings via LangChain vector store
