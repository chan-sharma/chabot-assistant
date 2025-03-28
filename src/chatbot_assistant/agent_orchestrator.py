from chatbot_assistant.ai_bot import Aibot

class AIAgent:
    """
    Orchestrator that delegates tasks to different business logic classes.
    """

    def __init__(self, aibot: Aibot):
        """
        Initialize the agent with both Summarizer and SummarizerChunk.
        """
        #self.client = OpenAIClient(OPENAI_AUTH)  # Pass the OpenAI object
        #self.headers = HEADERS

        # Injecting aibot here as DI
        self.aibot = aibot
    def chat (self, message: str, history: list):
        """
        Handles chat interactions by streaming responses from OpenAIClient.

        :param message: The user's input message.
        :param history: A list of previous messages in the conversation.
        :yield: The streamed response from the OpenAI API.
        """
        return self.aibot.chat(message, history)

   