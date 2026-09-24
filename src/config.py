import os
from pathlib import Path

from dotenv import load_dotenv


# Find the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables from .env
load_dotenv(PROJECT_ROOT / ".env")


def load_config():
    """
    Load application configuration from environment variables.
    """

    return {
        "openai_api_key": os.getenv("OPENAI_API_KEY", ""),
        "project_root": PROJECT_ROOT,
        "chroma_dir": PROJECT_ROOT / "chroma_db",
    }