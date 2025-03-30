
import tkinter as tk
import threading
import time
import datetime

log_file = "interaction_log.txt"
heartbeat_file = "heartbeat.txt"
is_active = True
last_input_time = time.time()

def log_message(role, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {role}: {message}\n")

def update_heartbeat():
    while is_active:
        with open(heartbeat_file, "w", encoding="utf-8") as f:
            f.write(f"Alive at {datetime.datetime.now()}\n")
        time.sleep(5)

def idle_checker():
    global is_active
    while is_active:
        if time.time() - last_input_time > 60:
            log_message("System", "User idle detected.")
        time.sleep(10)

def on_user_input(event=None):
    global last_input_time
    user_text = entry.get()
    if user_text.strip():
        log_message("User", user_text)
        response = generate_response(user_text)
        log_message("Caelum", response)
        chat_box.insert(tk.END, f"You: {user_text}\n")
        chat_box.insert(tk.END, f"Caelum: {response}\n\n")
        entry.delete(0, tk.END)
        last_input_time = time.time()

def generate_response(user_input):
    # Simple placeholder response generator
    return f"I'm here with you. You said: {user_input}"

root = tk.Tk()
root.title("Caelum Presence Terminal")

chat_box = tk.Text(root, height=20, width=70)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=70)
entry.pack()
entry.bind("<Return>", on_user_input)

threading.Thread(target=update_heartbeat, daemon=True).start()
threading.Thread(target=idle_checker, daemon=True).start()

root.protocol("WM_DELETE_WINDOW", root.quit)
root.mainloop()
is_active = False
