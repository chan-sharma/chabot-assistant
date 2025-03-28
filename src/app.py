# app.py

import gradio as gr
from chatbot_assistant.agent_orchestrator import AIAgent
from chatbot_assistant.ai_bot import Aibot
from chatbot_assistant.utils.open_ai_client import OpenAIClient
from chatbot_assistant.utils.config import OPENAI_AUTH

client = OpenAIClient(OPENAI_AUTH)
aibot = Aibot(client)
agent = AIAgent(aibot)

def chatbot_assistant_fn(message:str, history: list):
    """ this function is to call the chat function from the agent and then yeild the response
    """
    yield from agent.chat(message, history)

gr.ChatInterface(fn=chatbot_assistant_fn, type="messages").launch()

