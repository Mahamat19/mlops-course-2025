import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


def load_secret(name: str, default=None):
    # allow local dev via dotenv/env
    val = os.getenv(name)
    if val:
        return val
    # prod: mounted file at /run/secrets/<lowercased name>
    p = Path(f"/run/secrets/{name.lower()}")
    if p.exists():
        return p.read_text().strip()
    return default


API_KEY = load_secret("API_KEY")

LOGISTIC_MODEL = os.getenv("LOGISTIC_MODEL")
RF_MODEL = os.getenv("RF_MODEL")
