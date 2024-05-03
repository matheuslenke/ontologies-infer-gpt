import asyncio

from local_infer import LocalInfer
from parser import load_ontologies
from src.gpt_infer import GPTInfer


# This function executes a user prompt calling OpenAI GPT API and with the instructions provided to infer types
async def run_gpt_stereotype_infer():
    infer = GPTInfer(local_api_key=False)
    while True:
        user_prompt = input("Please write some input to infer stereotypes: \n")
        response = await infer.get_completion(user_prompt=user_prompt)
        print(response)
    return 0


if __name__ == "__main__":
    asyncio.run(run_gpt_stereotype_infer())
    # load_ontologies()