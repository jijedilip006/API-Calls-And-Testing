import tkinter as tk
from GUI import ChatWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatWindow(root)
    if hasattr(app, 'chat_agent'): # Only run mainloop if initialization succeeded
        root.mainloop()