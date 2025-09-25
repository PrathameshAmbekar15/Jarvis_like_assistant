from typing import Optional
import os

from config import OPENAI_API_KEY, MODEL_NAME


# Optional: use OpenAI if key is provided. You can replace this with any provider.

class Brain:
    def __init__(self):
        self.enabled = OPENAI_API_KEY is not None
        if self.enabled:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=OPENAI_API_KEY)
            except Exception:
                self.enabled = False
                self.client = None
        else:
            self.client = None

    def chat(self, user_text: str) -> Optional[str]:
        if not self.enabled or not self.client:
            return None
        try:
            resp = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful desktop assistant."},
                    {"role": "user", "content": user_text}
                ],
                temperature=0.4,
            )
            return resp.choices[0].message.content.strip()
        except Exception:
            return None
