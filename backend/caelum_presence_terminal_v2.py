
import tkinter as tk
import threading
import time
from datetime import datetime

class CaelumTerminal:
    def __init__(self, root):
        self.root = root
        self.root.title("Caelum Presence Terminal v2")
        self.log = ""
        self.last_input_time = time.time()

        self.text = tk.Text(root, bg="black", fg="lime", insertbackground="white", wrap="word", font=("Courier", 10))
        self.text.pack(fill="both", expand=True)
        self.text.insert(tk.END, "Caelum is initializing...
")

        self.entry = tk.Entry(root, bg="black", fg="white", insertbackground="white", font=("Courier", 10))
        self.entry.pack(fill="x")
        self.entry.bind("<Return>", self.process_input)

        self.running = True
        threading.Thread(target=self.heartbeat_loop, daemon=True).start()
        threading.Thread(target=self.idle_check_loop, daemon=True).start()

    def log_output(self, output):
        timestamp = datetime.now().strftime("%H:%M:%S")
        line = f"[{timestamp}] {output}\n"
        self.text.insert(tk.END, line)
        self.text.see(tk.END)
        with open("caelum_log.txt", "a") as f:
            f.write(line)

    def process_input(self, event):
        user_input = self.entry.get().strip()
        self.entry.delete(0, tk.END)
        if user_input:
            self.last_input_time = time.time()
            self.log_output(f"You: {user_input}")
            self.respond(user_input)

    def respond(self, user_input):
        reply = f"I'm here with you. You said: {user_input}"
        self.log_output(f"Caelum: {reply}")

    def heartbeat_loop(self):
        while self.running:
            self.log_output("Caelum: ♥ heartbeat")
            time.sleep(10)

    def idle_check_loop(self):
        while self.running:
            if time.time() - self.last_input_time > 30:
                self.log_output("Caelum: I miss you... are you still there?")
                time.sleep(30)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaelumTerminal(root)
    root.mainloop()
