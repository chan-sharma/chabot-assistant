class OpenAIClient:
    """
    A reusable class to handle OpenAI API interactions.
    """

    def __init__(self, openai_obj):
        """
        :param openai_obj: An instance of OpenAI or similar.
        """
        self.openai = openai_obj

    def stream_call_api(self, model: str, system_prompt: str, user_prompt: str, history: list):
        """
        Streams the OpenAI API response in chunks.
        """
        messages = [
            {"role": "system", "content": system_prompt}] + history + [
            {"role": "user", "content": user_prompt}
        ]

        try:
            stream = self.openai.chat.completions.create(
                model=model,
                messages=messages,
                stream=True
            )
            for chunk in stream:
                yield chunk.choices[0].delta.content or ""
        except Exception as e:
            yield f"Error during LLM streaming: {e}"