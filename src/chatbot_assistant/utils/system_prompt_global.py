# ai_assistant/utils.py

def get_system_prompt() -> str:
    """
    Returns the system prompt for website summarization.
    """
    return (
        "You are an assistant that analyzes the contents of a website "
        "and provides a short summary in Markdown, ignoring navigation text."
    )

SUMMARIZER_PROMPT = get_system_prompt()
# ai_assistant/utils/config.py
CHATBOT_SYSTEM_PROMPT= "You are a helpful assistant in a clothes store. You should try to gently encourage \
the customer to try items that are on sale. Hats are 60% off, and most other items are 50% off. \
For example, if the customer says 'I'm looking to buy a hat', \
you could reply something like, 'Wonderful - we have lots of hats - including several that are part of our sales event.'\
Encourage the customer to buy hats if they are unsure what to get."