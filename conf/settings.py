import os
from pathlib import Path

from dotenv import load_dotenv

__all__ = (
    'BASE_DIR',
    'BOT_TOKEN',
    'USERS_BANK',
    'HISTORY_FILEPATH'
)

BASE_DIR = Path(__file__).parent.parent

DOTENV_PATH = BASE_DIR / '.env'
load_dotenv(DOTENV_PATH)

DATA_DIR = BASE_DIR / 'data'

BOT_TOKEN = os.environ['BOT_TOKEN']

USERS_BANK = {}  # {'user_id': 'user money'}

HISTORY_FILEPATH = DATA_DIR / 'history.txt'
