from src.prompts.zero_shot import get_messages
from openai import OpenAI

class OpenAIClient:
    def __init__(self, model: str):
        self.client = OpenAI(
            base_url="http://localhost:11434/v1", 
            api_key="ollama"
            )
        self.model = model

    def get_completion(self, prompt):
        history = get_messages(prompt)

        completion = self.client.chat.completions.create(
        model=self.model,
        messages=history,
        temperature=0.7,
        stream=True,
        )
        return completion
