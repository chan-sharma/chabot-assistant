import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv(override=True)

def get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("No API key found!")
    if not api_key.startswith("sk-proj-"):
        raise ValueError("API key doesn't start with 'sk-proj-'; check your .env.")
    return api_key

# Run the check and store the API key
API_KEY = get_api_key()

# Create and store the OpenAI object (if needed, pass the API key to the constructor)
OPENAI_AUTH = OpenAI()  # Adjust if your OpenAI instantiation requires API key

# Define common HTTP headers for requests
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}
# Default OpenAI model to use
DEFAULT_MODEL = "gpt-4o-mini"

# Default system prompt
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."

# Default user prompt template (can be formatted dynamically)
DEFAULT_USER_PROMPT_TEMPLATE = """
You are looking at a website titled: **{title}**

The contents of this website are as follows.
Please provide a short summary in **Markdown**.
If the website includes **news** or **announcements**, be sure to mention them.

---

{text}
"""