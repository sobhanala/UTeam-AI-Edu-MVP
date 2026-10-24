from abc import ABC, abstractmethod
from typing import List, Dict


class AgentInterface(ABC):
    @abstractmethod
    def send_message(self, user_id: str, message: str) -> str:
        pass

    @abstractmethod
    def get_history(self, user_id: str) -> List[Dict[str, str]]:
        pass
