from fastapi import APIRouter
import whisper
import pyttsx3

router = APIRouter()
model = whisper.load_model("base")
tts = pyttsx3.init()

@router.post("/stt")
def speech_to_text(audio_path: str):
    result = model.transcribe(audio_path)
    return {"text": result["text"]}

@router.post("/tts")
def text_to_speech(text: str):
    tts.say(text)
    tts.runAndWait()
    return {"status": "spoken"}