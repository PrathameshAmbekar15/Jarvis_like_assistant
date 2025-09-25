try:
    import pyttsx3  # optional
except ImportError:
    pyttsx3 = None

try:
    import speech_recognition as sr  # optional
except ImportError:
    sr = None


class VoiceIO:
    def __init__(self):
        # Setup text-to-speech engine if available
        if pyttsx3:
            self.tts = pyttsx3.init()
        else:
            self.tts = None

        # Setup speech recognizer if available
        if sr:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()
        else:
            self.recognizer = None
            self.microphone = None

    def speak(self, text: str):
        """Convert text to speech (if available), else print."""
        if self.tts:
            self.tts.say(text)
            self.tts.runAndWait()
        else:
            print(f"[Assistant]: {text}")

    def listen(self, prompt="You: "):
        """Listen from microphone if available, else use text input."""
        if self.recognizer and self.microphone:
            with self.microphone as source:
                print(prompt, end="", flush=True)
                audio = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return ""
        else:
            # fallback: text input
            return input(prompt)
