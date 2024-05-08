import asyncio
import pathlib
import string

import rdflib

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


async def run_local_stereotype_infer(user_prompt: string, filename: string):
    infer = LocalInfer()
    if user_prompt:
        response = await infer.get_completion(user_prompt=user_prompt)
        file = open(f"./out/results/{filename}.md", "w")
        file.write(response)
        file.close()
    else:
        while True:
            user_prompt = input("Please write some input to infer stereotypes: \n")
            response = await infer.get_completion(user_prompt=user_prompt)
            file = open(f"./out/{filename}.md", "a")
            file.write("\n")
            file.write(response)
            file.close()


def load_ontologies_classes():
    df = load_ontologies()
    return df


def write_ontologies_classes(df):
    # Save Elements to CSV
    file_object = open("./out/ontologies.csv", "w")
    columns_to_get = ['name', 'stereotype']
    for index, row in df.iterrows():  # Iterate over rows
        final_string = ""
        for column_name in columns_to_get:
            try:
                value = row[column_name]
                final_string = final_string + value + " ; "
            except Exception as e:
                print(e)
        final_string = final_string + " \n"
        file_object.write(final_string)
    file_object.close()


if __name__ == "__main__":
    all_dfs = load_ontologies_classes()
    # write_ontologies_classes(df)

    for index, df in enumerate(all_dfs):
        full_prompt = ""
        for item in df['name']:
            full_prompt = full_prompt + str(item) + ", "
        asyncio.run(run_local_stereotype_infer(user_prompt=full_prompt, filename=str(index)))
