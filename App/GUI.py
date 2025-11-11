import sys
import os
import tkinter as tk
from agent import GeminiChatAgent

# --- Path adjustment to ensure correct tkinter import ---
# Remove current directory from sys.path temporarily so "import tkinter"
# imports the system tkinter module instead of this local file.
_curdir = os.path.dirname(__file__) or os.getcwd()
_removed = False
if _curdir in sys.path:
    sys.path.remove(_curdir)
    _removed = True

# restore sys.path
if _removed:
    sys.path.insert(0, _curdir)
# --------------------------------------------------------

class ChatWindow:
    """
    Creates and manages the Tkinter GUI for the chat application.
    Integrates with the GeminiChatAgent for backend logic.
    """
    def __init__(self, root: tk.Tk):
        """Sets up the main window and initializes the chat agent."""
        self.root = root
        self.root.title("Gemini PDF Processor Chat")
        self.root.geometry("600x400")

        # 1. Initialize the AI Agent
        try:
            self.chat_agent = GeminiChatAgent()
        except (ValueError, RuntimeError) as e:
            self.root.destroy()
            return

        # 2. Setup the GUI layout
        self._create_widgets()
        
        # 3. Bind the Enter key to send_message
        self.entry.bind("<Return>", self._send_message_handler)
        self.entry.focus_set()

    def _create_widgets(self):
        """Creates all necessary Tkinter widgets."""
        
        # Main Frame
        main_frame = tk.Frame(self.root, relief="ridge", borderwidth=2)
        main_frame.pack(fill="both", expand=1, padx=6, pady=6)

        # Read-only text area for messages
        self.text_display = tk.Text(main_frame, wrap="word", state="disabled")
        self.text_display.pack(fill="both", expand=1, padx=4, pady=(4, 2))

        # Bottom frame for entry + send button
        bottom_frame = tk.Frame(main_frame)
        bottom_frame.pack(fill="x", pady=4)

        # Input Entry Field
        self.entry = tk.Entry(bottom_frame)
        self.entry.pack(side="left", fill="x", expand=1, padx=(4, 2))

        # Send Button
        send_btn = tk.Button(bottom_frame, text="Send", command=self._send_message_handler)
        send_btn.pack(side="right", padx=(2, 4))
        
    def _append_message(self, msg: str):
        """
        Adds a new message to the text display area.
        
        Args:
            msg (str): The message to be displayed.
        """
        self.text_display.config(state="normal")
        self.text_display.insert("end", msg + "\n")
        self.text_display.config(state="disabled")
        self.text_display.see("end")

    def _send_message_handler(self, event=None):
        """
        Handles sending of messages from the input field, interacts with the agent, 
        and updates the display.
        
        Args:
            event: Optional key event when triggered by Enter key.
            
        Returns:
            str: "break" to prevent default Enter key behavior.
        """
        user_prompt = self.entry.get().strip()
        
        if not user_prompt:
            return "break"
            
        # 1. Display user message
        self._append_message("You: " + user_prompt)
        
        # 2. Clear entry field
        self.entry.delete(0, "end")
        
        # 3. Get AI response (can block the GUI, but simple for this example)
        # For a production app, this should run on a separate thread/executor
        ai_response = self.chat_agent.send_message(user_prompt)
        
        # 4. Display AI response
        self._append_message("AI: " + ai_response)
        
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatWindow(root)
    if hasattr(app, 'chat_agent'): # Only run mainloop if initialization succeeded
        root.mainloop()