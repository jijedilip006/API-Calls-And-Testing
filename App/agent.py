import os
from google import genai

class GeminiChatAgent:
    """
    Handles initialization and interaction with the Google Gemini API.
    Manages the chat session state.
    """
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        """Initializes the Gemini client and starts a new chat session."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable not set. "
                "Please set it before running the application."
            )
        try:
            self.client = genai.Client(api_key=api_key)
            self.chat = self.client.chats.create(model=model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Gemini Client or Chat: {e}")

    def send_message(self, prompt: str) -> str:
        """
        Sends a message to the Gemini model and returns the response text.

        Args:
            prompt (str): The user's message.

        Returns:
            str: The AI's response text.
        """
        try:
            response = self.chat.send_message(prompt)
            return str(response.text)
        except Exception as e:
            return f"An unexpected error occurred: {e}"