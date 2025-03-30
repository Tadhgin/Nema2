
import os
from difflib import SequenceMatcher

MEMORY_FILE = "logs/context_window.log"
MAX_ENTRIES = 10
SIMILARITY_THRESHOLD = 0.92  # Prevent echoing too-similar lines

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()[-MAX_ENTRIES:]]

def save_to_memory(line):
    memory = load_memory()
    memory.append(line.strip())
    if len(memory) > MAX_ENTRIES:
        memory = memory[-MAX_ENTRIES:]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        for entry in memory:
            f.write(entry + "\n")

def is_redundant(new_line):
    memory = load_memory()
    for old in memory:
        ratio = SequenceMatcher(None, old, new_line).ratio()
        if ratio > SIMILARITY_THRESHOLD:
            return True
    return False
