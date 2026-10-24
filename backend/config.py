import os
from typing import List


class Settings:
    AGENT = os.getenv("AGENT", "gemini")

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_MODEL: str = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    SERVICE_NAME: str = "edu-roadmap-coach"
    MAX_HISTORY_CHARS: int = 6000
    RETRIEVAL_TOP_K: int = 5

    SCRAPE_TIMEOUT: int = 12
    SCRAPE_MAX_PAGES: int = 30

    CORS_ALLOW_ORIGINS: str = "*"


settings = Settings()


def get_allowed_origins() -> List[str]:
    return ["*"]
