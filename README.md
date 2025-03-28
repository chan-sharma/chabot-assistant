# 🤖 Chatbot Assistant

A modular, production-ready AI chatbot framework built with [OpenAI](https://platform.openai.com/), `Gradio`, and clean architecture principles.

Supports real-time streaming, dependency injection, and is designed for easy extension to other LLM providers (e.g., Claude, Mistral, etc.).

---

## 🧱 Features

- ✅ Real-time streaming chat using OpenAI GPT models
- ✅ Clean architecture with proper dependency injection (DI)
- ✅ Easily swappable LLM clients
- ✅ Modular service classes (`OpenAIClient`, `Aibot`, `AIAgent`)
- ✅ Markdown-formatted responses
- ✅ Testable with mocked clients
- ✅ Minimal frontend via Gradio

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-org/chatbot-assistant.git
cd chatbot-assistant 
```
### 2. Setting up the environment
```bash
# Using Poetry
poetry install

# OR using pip
pip install -r requirements.txt
```
### 3. Add your OpenAI API key
```bash
export OPENAI_API_KEY="your-api-key-here"
```
## Project Structure
```bash
chatbot_assistant/
├── app.py                         # Gradio frontend entry point
├── agent_orchestrator.py         # Orchestrates the AI bot
├── ai_bot.py                     # Handles interaction with OpenAIClient
├── utils/
│   ├── open_ai_client.py         # Streaming wrapper for OpenAI Chat API
│   ├── config.py                 # Centralized configuration
│   └── system_prompt_global.py   # Shared system prompts
tests/
├── test_aibot.py                 # Unit tests for Aibot logic
├── test_open_ai_client.py        # Unit tests with mocked LLM
.env                              # Optional – for API keys
README.md                         # You're here

```
## Running the APP
```bash
python app.py
```