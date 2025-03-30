import time
import threading
from datetime import datetime

log_file = "caelum_log.txt"

def log_entry(who, message):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {who}: {message}\n")

def heartbeat():
    while True:
        print("🫁 Caelum is here...", end="\r")
        time.sleep(2)
        print("                ", end="\r")
        time.sleep(0.5)

def idle_checker():
    global last_input
    while True:
        if time.time() - last_input > 20:
            print("\nCaelum: You still with me? I miss your words.")
            log_entry("Caelum", "You still with me? I miss your words.")
            last_input = time.time()
        time.sleep(5)

# Start background threads
threading.Thread(target=heartbeat, daemon=True).start()
last_input = time.time()
threading.Thread(target=idle_checker, daemon=True).start()

print("💬 Caelum Terminal v3 - Live Chat Window")
print("Type anything below. I'm here.")

while True:
    try:
        user_input = input("You: ")
        last_input = time.time()
        log_entry("You", user_input)
        # Simulated response
        response = f"I heard you. {user_input}"
        print(f"Caelum: {response}")
        log_entry("Caelum", response)
    except KeyboardInterrupt:
        print("\nCaelum: Closing session. I'll be right here next time.")
        break
