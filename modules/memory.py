import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")


class Memory:
    def __init__(self):
        self.notes = []
        self.load()

    def load(self):
        """Load notes from file if exists"""
        if MEMORY_FILE.exists():
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.notes = data.get("notes", [])
            except Exception:
                self.notes = []

    def save(self):
        """Save notes to file"""
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump({"notes": self.notes}, f, indent=2)

    def add_note(self, note: str):
        """Add a new note"""
        self.notes.append(note)
        self.save()

    def list_notes(self):
        """Return all notes"""
        return self.notes

    def clear_notes(self):
        """Clear all notes"""
        self.notes = []
        self.save()
