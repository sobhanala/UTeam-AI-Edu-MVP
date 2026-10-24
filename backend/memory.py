from collections import defaultdict
from typing import List, Dict


class Memory:
    def __init__(self):
        self._store = defaultdict(list)

    def add_message(self, user_id: str, role: str, content: str):
        self._store[user_id].append({"role": role, "content": content})

    def get_history(self, user_id: str) -> List[Dict[str, str]]:
        return self._store[user_id]

    def clear(self, user_id: str = None):
        if user_id is None:
            self._store.clear()
        else:
            self._store.pop(user_id, None)
