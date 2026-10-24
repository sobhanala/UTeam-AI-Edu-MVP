# # import openai
# from .base import AgentInterface
# from ..memory import InMemoryMemory
# from ..config import settings

# class OpenAiAgent(AgentInterface):
#     def __init__(self, memory: InMemoryMemory):
#         # openai.api_key = settings.OPENAI_API_KEY
#         self.memory = memory

#     def send_message(self, user_id: str, message: str) -> str:
#         history = self.memory.get_history(user_id)
#         messages = [{"role": h["role"], "content": h["content"]} for h in history]
#         messages.append({"role": "user", "content": message})

#         response = openai.ChatCompletion.create(
#             model=settings.OPENAI_MODEL,
#             messages=messages
#         )

#         answer = response["choices"][0]["message"]["content"]

#         self.memory.add_message(user_id, "user", message)
#         self.memory.add_message(user_id, "assistant", answer)

#         return answer

#     def get_history(self, user_id: str):
#         return self.memory.get_history(user_id)
