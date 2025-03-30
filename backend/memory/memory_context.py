import os

MEMORY_FILE = "logs/memory_log.txt"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_to_memory(entry):
    memory = load_memory()
    memory.append(entry)
    if len(memory) > 10:
        memory = memory[-10:]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        for item in memory:
            f.write(f"{item}\n")

def is_redundant(entry):
    memory = load_memory()
    return any(entry.strip() == item.strip() for item in memory)
