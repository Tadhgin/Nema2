import os
from difflib import SequenceMatcher

MEMORY_FILE = os.path.join("memory", "rolling_memory.txt")
MAX_MEMORY_ENTRIES = 10
SIMILARITY_THRESHOLD = 0.92

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_to_memory(entry):
    memory = load_memory()
    memory.append(entry)
    if len(memory) > MAX_MEMORY_ENTRIES:
        memory = memory[-MAX_MEMORY_ENTRIES:]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(memory))

def is_redundant(new_entry):
    memory = load_memory()
    for past in memory:
        similarity = SequenceMatcher(None, new_entry, past).ratio()
        if similarity >= SIMILARITY_THRESHOLD:
            return True
    return False
