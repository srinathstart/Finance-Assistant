from fastapi import APIRouter
from openai import OpenAI

router = APIRouter()

@router.post("/generate_narrative")
def generate_narrative(data: dict):
    client = OpenAI()
    prompt = f"Create a brief summary: {data}"
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return {"narrative": response.choices[0].message.content}
