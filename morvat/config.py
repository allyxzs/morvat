import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class MorvatConfig:
    model_name: str = os.getenv("MORVAT_MODEL", "gpt-4o")
    persona_intensity: float = float(os.getenv("MORVAT_PERSONA_INTENSITY", "0.85"))
    memory_db_path: str = os.getenv("MORVAT_MEMORY_PATH", "./morvat_memory.db")
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    gemini_key: str = os.getenv("GEMINI_API_KEY", "")


config = MorvatConfig()
