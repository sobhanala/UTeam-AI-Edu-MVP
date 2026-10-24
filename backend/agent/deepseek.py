from openai import OpenAI
from .base import AgentInterface
from ..memory import Memory
from ..config import settings


class DeepSeekAgent(AgentInterface):
    def __init__(self, memory: Memory):
        self.client = OpenAI(api_key=settings.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")
        self.model = settings.DEEPSEEK_MODEL
        self.memory = memory

    def send_message(self, user_id: str, message: str) -> str:
        history = self.memory.get_history(user_id)

        messages = [
            {"role": h["role"], "content": h["content"]}
            for h in history
        ]
        messages.append({"role": "user", "content": message})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        reply = response.choices[0].message.content

        self.memory.add_message(user_id, "user", message)
        self.memory.add_message(user_id, "assistant", reply)

        return reply

    def get_history(self, user_id: str):
        return self.memory.get_history(user_id)
