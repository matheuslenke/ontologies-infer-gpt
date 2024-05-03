import string

from azure_authentication_client import authenticate_device_flow
from langchain.chains import LLMChain
from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.callbacks import StreamingStdOutCallbackHandler


class LLMClient:
    def __init__(self, host, port, model: string, is_local: bool = False, local_api_key: bool = True):
        if is_local:
            self.client = Ollama(model="llama2")
        else:
            LLMClient.use_local_api_key()
            # self.client.api_key = os.getenv('OPENAI_API_KEY')
            # Authentication with Accenture Lib
            authenticate_device_flow()
            self.client = ChatOpenAI(
                callbacks=[StreamingStdOutCallbackHandler()],
                streaming=True
            )

    @staticmethod
    def use_local_api_key():
        _ = load_dotenv(find_dotenv())  # read local .env file

    def get_completion(self, prompt):
        chain = LLMChain(llm=self.client, prompt=prompt)
        chain.run()
