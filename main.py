import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

# Load .env
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Qwen Agent PoC",
    version="1.0.0",
)

# Create Qwen client
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)


# -----------------------------
# Models
# -----------------------------

class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


class ChatResponse(BaseModel):
    response: str


# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def root():
    return {
        "status": "running",
        "service": "Qwen Agent PoC",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="qwen3.7-plus",
            messages=[
                message.model_dump()
                for message in request.messages
            ],
        )

        return ChatResponse(
            response=completion.choices[0].message.content
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )