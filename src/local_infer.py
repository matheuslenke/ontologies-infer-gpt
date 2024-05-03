import string

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from prompts import zero_shot


class LocalInfer(object):
    def __init__(self):
        self.llm = Ollama(model="llama2")
        self.embeddings = OllamaEmbeddings()

    def create_embeddings(self):
        loader = PyPDFLoader("../docs/papers/tonto.pdf")
        pages = loader.load_and_split()
        text_splitter = RecursiveCharacterTextSplitter()
        documents = text_splitter.split_documents()

    async def get_local_completion(self, user_prompt: string):
        prompt = ChatPromptTemplate.from_messages(zero_shot.get_messages_tuple(prompt=user_prompt))

        chain = prompt | self.llm
        chunks = []
        async for chunk in chain.astream({"input": f"####{user_prompt}####"}):
            chunks.append(chunk)
            print(chunk, end="")
        return chunks


    # def save_to_file(self, chunks: [string]):
    #     with open("../out/results.txt", "w") as outfile:
    #         for chunk in chunks:
    #             print(chunk)