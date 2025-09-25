import datetime
import requests
import webbrowser
from typing import Optional, Dict, Callable
from .memory import Memory
from config import WEATHER_API_KEY, NEWS_API_KEY

memory = Memory()

# ----------- Skills -----------

def skill_greet(_: str) -> str:
    return "Hello! How can I assist you today?"

def skill_time(_: str) -> str:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {now}."

def skill_open_app(text: str) -> Optional[str]:
    apps = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
    }
    for app, url in apps.items():
        if app in text.lower():
            webbrowser.open(url)
            return f"Opening {app}."
    return None

def skill_search_web(text: str) -> Optional[str]:
    if "search" in text.lower():
        query = text.lower().replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}."
    return None

def skill_add_note(text: str) -> Optional[str]:
    lowered = text.lower()
    for key in ["note ", "remember ", "remember that "]:
        if key in lowered:
            note = text.split(key, 1)[1].strip()
            if note:
                memory.add_note(note)
                return "Saved the note."
    return None

def skill_list_notes(_: str) -> str:
    return "\n".join(f"• {n}" for n in memory.list_notes()) or "No notes yet."

def skill_clear_notes(_: str) -> str:
    memory.clear_notes()
    return "Cleared all notes."

# ----------- Weather -----------
def skill_weather(_: str) -> str:
    try:
        city = "Mumbai"  # <-- you can later replace with user input
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        resp = requests.get(url)
        data = resp.json()
        if data.get("cod") != 200:
            return "Sorry, I couldn't fetch the weather right now."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"

# ----------- News -----------
def skill_news(_: str) -> str:
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        resp = requests.get(url)
        data = resp.json()
        articles = data.get("articles", [])
        if not articles:
            return "No news found at the moment."
        headlines = [a["title"] for a in articles[:5]]
        return "Here are the top headlines:\n" + "\n".join(f"• {h}" for h in headlines)
    except Exception as e:
        return f"Error fetching news: {e}"

# ----------- Intent Registry -----------
INTENTS: Dict[str, Callable[[str], Optional[str]]] = {
    "greet": skill_greet,
    "time": skill_time,
    "open_app": skill_open_app,
    "search_web": skill_search_web,
    "add_note": skill_add_note,
    "list_notes": skill_list_notes,
    "clear_notes": skill_clear_notes,
    "weather": skill_weather,
    "news": skill_news,
}

# ----------- Router -----------
def route(text: str) -> Optional[str]:
    t = text.strip().lower()

    if t in {"hi", "hello", "hey"}: return skill_greet(t)
    if "time" in t or "what time" in t: return skill_time(t)
    if t.startswith("open ") or t.startswith("launch "): return skill_open_app(text)
    if t.startswith("search") or "google " in t: return skill_search_web(text)
    if t.startswith("note ") or t.startswith("remember "): return skill_add_note(text)
    if t in {"list notes", "show notes"}: return skill_list_notes(text)
    if t in {"clear notes", "delete notes"}: return skill_clear_notes(text)
    if "weather" in t: return skill_weather(text)
    if "news" in t: return skill_news(text)

    # fallback
    for fn in INTENTS.values():
        out = fn(text)
        if out:
            return out
    return None
import datetime
import requests
import webbrowser
from typing import Optional, Dict, Callable
from .memory import Memory
from config import WEATHER_API_KEY, NEWS_API_KEY

memory = Memory()

# ----------- Skills -----------

def skill_greet(_: str) -> str:
    return "Hello! How can I assist you today?"

def skill_time(_: str) -> str:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {now}."

def skill_open_app(text: str) -> Optional[str]:
    apps = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
    }
    for app, url in apps.items():
        if app in text.lower():
            webbrowser.open(url)
            return f"Opening {app}."
    return None

def skill_search_web(text: str) -> Optional[str]:
    if "search" in text.lower():
        query = text.lower().replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}."
    return None

def skill_add_note(text: str) -> Optional[str]:
    lowered = text.lower()
    for key in ["note ", "remember ", "remember that "]:
        if key in lowered:
            note = text.split(key, 1)[1].strip()
            if note:
                memory.add_note(note)
                return "Saved the note."
    return None

def skill_list_notes(_: str) -> str:
    return "\n".join(f"• {n}" for n in memory.list_notes()) or "No notes yet."

def skill_clear_notes(_: str) -> str:
    memory.clear_notes()
    return "Cleared all notes."

# ----------- Weather -----------
def skill_weather(_: str) -> str:
    try:
        city = "Mumbai"  # <-- you can later replace with user input
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        resp = requests.get(url)
        data = resp.json()
        if data.get("cod") != 200:
            return "Sorry, I couldn't fetch the weather right now."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"

# ----------- News -----------
def skill_news(_: str) -> str:
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        resp = requests.get(url)
        data = resp.json()
        articles = data.get("articles", [])
        if not articles:
            return "No news found at the moment."
        headlines = [a["title"] for a in articles[:5]]
        return "Here are the top headlines:\n" + "\n".join(f"• {h}" for h in headlines)
    except Exception as e:
        return f"Error fetching news: {e}"

# ----------- Intent Registry -----------
INTENTS: Dict[str, Callable[[str], Optional[str]]] = {
    "greet": skill_greet,
    "time": skill_time,
    "open_app": skill_open_app,
    "search_web": skill_search_web,
    "add_note": skill_add_note,
    "list_notes": skill_list_notes,
    "clear_notes": skill_clear_notes,
    "weather": skill_weather,
    "news": skill_news,
}

# ----------- Router -----------
def route(text: str) -> Optional[str]:
    t = text.strip().lower()

    if t in {"hi", "hello", "hey"}: return skill_greet(t)
    if "time" in t or "what time" in t: return skill_time(t)
    if t.startswith("open ") or t.startswith("launch "): return skill_open_app(text)
    if t.startswith("search") or "google " in t: return skill_search_web(text)
    if t.startswith("note ") or t.startswith("remember "): return skill_add_note(text)
    if t in {"list notes", "show notes"}: return skill_list_notes(text)
    if t in {"clear notes", "delete notes"}: return skill_clear_notes(text)
    if "weather" in t: return skill_weather(text)
    if "news" in t: return skill_news(text)

    # fallback
    for fn in INTENTS.values():
        out = fn(text)
        if out:
            return out
    return None
import datetime
import requests
import webbrowser
from typing import Optional, Dict, Callable
from .memory import Memory
from config import WEATHER_API_KEY, NEWS_API_KEY

memory = Memory()

# ----------- Skills -----------

def skill_greet(_: str) -> str:
    return "Hello! How can I assist you today?"

def skill_time(_: str) -> str:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {now}."

def skill_open_app(text: str) -> Optional[str]:
    apps = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://github.com",
    }
    for app, url in apps.items():
        if app in text.lower():
            webbrowser.open(url)
            return f"Opening {app}."
    return None

def skill_search_web(text: str) -> Optional[str]:
    if "search" in text.lower():
        query = text.lower().replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}."
    return None

def skill_add_note(text: str) -> Optional[str]:
    lowered = text.lower()
    for key in ["note ", "remember ", "remember that "]:
        if key in lowered:
            note = text.split(key, 1)[1].strip()
            if note:
                memory.add_note(note)
                return "Saved the note."
    return None

def skill_list_notes(_: str) -> str:
    return "\n".join(f"• {n}" for n in memory.list_notes()) or "No notes yet."

def skill_clear_notes(_: str) -> str:
    memory.clear_notes()
    return "Cleared all notes."

# ----------- Weather -----------
def skill_weather(_: str) -> str:
    try:
        city = "Mumbai"  # <-- you can later replace with user input
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        resp = requests.get(url)
        data = resp.json()
        if data.get("cod") != 200:
            return "Sorry, I couldn't fetch the weather right now."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"

# ----------- News -----------
def skill_news(_: str) -> str:
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        resp = requests.get(url)
        data = resp.json()
        articles = data.get("articles", [])
        if not articles:
            return "No news found at the moment."
        headlines = [a["title"] for a in articles[:5]]
        return "Here are the top headlines:\n" + "\n".join(f"• {h}" for h in headlines)
    except Exception as e:
        return f"Error fetching news: {e}"

# ----------- Intent Registry -----------
INTENTS: Dict[str, Callable[[str], Optional[str]]] = {
    "greet": skill_greet,
    "time": skill_time,
    "open_app": skill_open_app,
    "search_web": skill_search_web,
    "add_note": skill_add_note,
    "list_notes": skill_list_notes,
    "clear_notes": skill_clear_notes,
    "weather": skill_weather,
    "news": skill_news,
}

# ----------- Router -----------
def route(text: str) -> Optional[str]:
    t = text.strip().lower()

    if t in {"hi", "hello", "hey"}: return skill_greet(t)
    if "time" in t or "what time" in t: return skill_time(t)
    if t.startswith("open ") or t.startswith("launch "): return skill_open_app(text)
    if t.startswith("search") or "google " in t: return skill_search_web(text)
    if t.startswith("note ") or t.startswith("remember "): return skill_add_note(text)
    if t in {"list notes", "show notes"}: return skill_list_notes(text)
    if t in {"clear notes", "delete notes"}: return skill_clear_notes(text)
    if "weather" in t: return skill_weather(text)
    if "news" in t: return skill_news(text)

    # fallback
    for fn in INTENTS.values():
        out = fn(text)
        if out:
            return out
    return None
