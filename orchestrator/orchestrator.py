from fastapi import FastAPI
from agents import api_agent, scraping_agent, retriever_agent, analysis_agent, language_agent, voice_agent

app = FastAPI()

app.include_router(api_agent.router)
app.include_router(scraping_agent.router)
app.include_router(retriever_agent.router)
app.include_router(analysis_agent.router)
app.include_router(language_agent.router)
app.include_router(voice_agent.router)