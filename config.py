import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("f4482127beb265ef7f7bb251294e5abf")
NEWS_API_KEY = os.getenv("e9ba34a7a84b452b9605434f8c8d9782")

ASSISTANT_NAME = "Jarvis"
WAKE_WORDS = ["jarvis", "assistant"]
MODEL_NAME = "gpt-3.5-turbo"