import sys
import os

# Remove current directory from sys.path temporarily so "import tkinter"
# imports the system tkinter module instead of this local file.
_curdir = os.path.dirname(__file__) or os.getcwd()
_removed = False
if _curdir in sys.path:
    sys.path.remove(_curdir)
    _removed = True

import tkinter as tk

# restore sys.path
if _removed:
    sys.path.insert(0, _curdir)

def create_chat_window():
    root = tk.Tk()
    root.title("Simple Chat")
    root.geometry("600x400")

    frame = tk.Frame(root, relief="ridge", borderwidth=2)
    frame.pack(fill="both", expand=1, padx=6, pady=6)

    # Read-only text area for messages
    text_display = tk.Text(frame, wrap="word", state="disabled")
    text_display.pack(fill="both", expand=1, padx=4, pady=(4,2))

    # Bottom frame for entry + send button
    bottom = tk.Frame(frame)
    bottom.pack(fill="x", pady=4)

    entry = tk.Entry(bottom)
    entry.pack(side="left", fill="x", expand=1, padx=(4,2))

    def append_message(msg: str):
        text_display.config(state="normal")
        text_display.insert("end", msg + "\n")
        text_display.config(state="disabled")
        text_display.see("end")

    def send_message(event=None):
        msg = entry.get().strip()
        if not msg:
            return "break"
        append_message("You: " + msg)
        entry.delete(0, "end")
        return "break"

    send_btn = tk.Button(bottom, text="Send", command=send_message)
    send_btn.pack(side="right", padx=(2,4))

    entry.bind("<Return>", send_message)
    entry.focus_set()

    root.mainloop()

if __name__ == "__main__":
    create_chat_window()