import string

from src.client.gemini_client import GeminiClient
from src.client.llm_client import LLMClient
from prompts.zero_shot import get_messages
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class GeminiInfer(object):

    def __init__(self, api_key: string):
        self.client = GeminiClient(api_key=api_key)

    def get_completion(self, user_prompt):
        response = self.client.get_completion(prompt=user_prompt)