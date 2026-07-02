from fastapi import APIRouter

from app.models.schemas import ChatRequest, ChatResponse
from app.agent.agent import SHLAgent

router = APIRouter()

agent = SHLAgent()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return agent.chat(request.messages)

@router.get("/")
def root():
    return {
        "service": "SHL Assessment Recommendation Agent",
        "status": "running",
        "docs": "/docs"
    }