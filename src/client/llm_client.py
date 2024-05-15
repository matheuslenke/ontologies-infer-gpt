import os
import string

# from azure_authentication_client import authenticate_device_flow
from langchain.chains import LLMChain
from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.callbacks import StreamingStdOutCallbackHandler

from src.prompts import zero_shot


class LLMClient:
    def __init__(self):
        LLMClient.use_local_api_key()
        # Authentication with Accenture Lib
        # authenticate_device_flow()
        self.llm = ChatOpenAI(
            callbacks=[StreamingStdOutCallbackHandler()],
            streaming=True,
        )
        self.llm.openai_api_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def use_local_api_key():
        _ = load_dotenv(find_dotenv())  # read local .env file

    def get_completion(self, prompt):
        prompt_dict = zero_shot.get_messages(prompt)
        response = self.llm.invoke(prompt_dict)
        return response.content
