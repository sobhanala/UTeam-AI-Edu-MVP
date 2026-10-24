import google.generativeai as genai
from .base import AgentInterface
from ..memory import Memory
from ..config import settings


class GeminiAgent(AgentInterface):
    def __init__(self, memory: Memory):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)
        self.memory = memory

    def send_message(self, user_id: str, message: str) -> str:
        history = self.memory.get_history(user_id)

        chat = self.model.start_chat(
            history=[{"role": h["role"], "parts": [h["content"]]} for h in history]
        )

        response = chat.send_message(message)

        self.memory.add_message(user_id, "user", message)
        self.memory.add_message(user_id, "assistant", response.text)

        return response.text

    def get_history(self, user_id: str):
        return self.memory.get_history(user_id)
