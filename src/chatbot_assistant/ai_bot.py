from chatbot_assistant.utils.open_ai_client import OpenAIClient
from chatbot_assistant.utils.system_prompt_global import CHATBOT_SYSTEM_PROMPT

class Aibot:
    """
    Contains logic for streaming summarization of a website using an LLM (e.g., OpenAI).
    """

    def __init__(self, client: OpenAIClient):
        """
        :param client: An instance of OpenAIClient.
        :param headers: A dict of headers to use for HTTP requests.
        """
        self.client = client  # Injected dependency
        #self.headers = headers
        self.system_prompt =CHATBOT_SYSTEM_PROMPT  # Use the global system prompt
 

    def chat(self, message: str, history: list):
        """
        Handles chat interactions by streaming responses from OpenAIClient.

        :param message: The user's input message.
        :param history: A list of previous messages in the conversation.
        :yield: The streamed response from the OpenAI API.
        """
        try:

            stream = self.client.stream_call_api(
                model="gpt-4",  # Replace with your default model
                system_prompt=self.system_prompt,
                user_prompt=message,
                history=history,
                #stream=True
            )
            response = ""
            for chunk in stream:
                response += chunk
                yield response  # Stream the response incrementally
        except Exception as e:
            yield f"Error during chat processing: {e}"