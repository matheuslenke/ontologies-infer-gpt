from src.client.llm_client import LLMClient
from prompts.zero_shot import get_messages
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


class GPTInfer(object):

    def __init__(self, local_api_key: bool):
        self.client = LLMClient()

    async def get_completion(self, user_prompt, model="gpt-3.5-turbo"):
        response = self.client.get_completion(prompt=user_prompt)
        return response
