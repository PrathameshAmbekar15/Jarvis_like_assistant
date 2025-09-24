from modules.voice import VoiceIO
from modules.brain import Brain
from modules.skills import route
from config import ASSISTANT_NAME, WAKE_WORDS


def main():
    io = VoiceIO()
    brain = Brain()

    io.speak(f"Hello, I'm {ASSISTANT_NAME}. Say my name or type a command. Type 'exit' to quit.")

    while True:
        user = io.listen(prompt="> ")

        if not user:
            continue

        if user.lower() in {"exit", "quit"}:
            io.speak("Goodbye!")
            break

        # Simple wake-word gate (for text mode): ignore input unless it contains wake word
        if not any(w in user.lower() for w in WAKE_WORDS) and user.count(" ") < 1:
            # encourage wake word for single tokens
            continue

        # Remove wake words from the front if present
        lowered = user.lower()
        for w in WAKE_WORDS:
            if lowered.startswith(w + " "):
                user = user[len(w)+1:]
                break

        # 1) Try local skills
        response = route(user)

        # 2) Fallback to LLM (if configured)
        if not response:
            response = brain.chat(user) or "I don't know that yet. Want me to learn it later?"

        io.speak(response)


if __name__ == "__main__":
    main()
