from __future__ import annotations

# FastAPI و ابزارهای مرتبط
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ماژول‌های پروژه (absolute import با prefix 'backend')
from backend.config import settings, get_allowed_origins
from backend.memory import Memory
from backend.prompt import build_prompt

# Agent ها
from backend.agent.gemini import GeminiAgent
from backend.agent.deepseek import DeepSeekAgent


app = FastAPI(title=settings.SERVICE_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MEMORY = Memory()


if settings.AGENT == "gemini":
    AGENT = GeminiAgent(memory=MEMORY)
    
elif settings.AGENT == "deepseek":
    AGENT = DeepSeekAgent(memory=MEMORY)

else:
    raise RuntimeError(f"Unsupported LLM provider: {settings.AGENT}")


class HealthResponse(BaseModel):
    status: str
    provider: str
    model: str | None
    

class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    answer: str


def detect_lang(text: str) -> str:
    for ch in text:
        if "\u0600" <= ch <= "\u06ff":
            return "fa"
    return "en"


# -------------------------
# Endpoints
# -------------------------
@app.get("/health", response_model=HealthResponse)
def health():
    return {
        "status": "ok",
        "provider": settings.AGENT,
        "model": getattr(settings, f"{settings.AGENT.upper()}_MODEL", None),
    }


@app.delete("/sessions/{session_id}")
def clear_session(session_id: str):
    MEMORY.clear(session_id)
    return {"cleared": True}


@app.get("/sessions/{session_id}")
def get_session(session_id: str):
    msgs = AGENT.memory.get_history(session_id)
    return {"messages": [{"role": m["role"], "content": m["content"]} for m in msgs]}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    lang = detect_lang(req.message)
    prompt = build_prompt(req.message, lang)

    try:
        answer = AGENT.send_message(req.session_id, prompt)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    return ChatResponse(answer=answer)
