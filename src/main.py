import asyncio
import os
import string
import csv

from local_infer import LocalInfer
from parser import load_ontologies
from src.gemini_infer import GeminiInfer
from src.gpt_infer import GPTInfer


# This function executes a user prompt calling OpenAI GPT API and with the instructions provided to infer types
async def run_gpt_stereotype_infer(user_prompt: string, filename: string):
    infer = GPTInfer(local_api_key=True)
    local_response = await infer.get_completion(user_prompt=user_prompt)
    return local_response


async def run_gemini_stereotype_infer(user_prompt: string, filename: string):
    api_key = os.getenv("GEMINI_API_KEY")
    infer = GeminiInfer(api_key=api_key)
    if user_prompt:
        response = await infer.get_completion(user_prompt=user_prompt)
        file = open(f"./out/results-gemini/{filename}.md", "w")
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


async def run_local_stereotype_infer(user_prompt: string, filename: string):
    infer = LocalInfer()
    if user_prompt:
        print(user_prompt)
        response = await infer.get_completion(user_prompt=user_prompt)
        return response
        # file = open(f"./out/results-local/{filename}.md", "w")
        # file.write(response)
        # file.close()
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


def read_csv_elements(filename):
    """Reads a CSV file and extracts the first and second elements from the first row.

    Args:
        filename: The path to the CSV file.

    Returns:
        A tuple containing the first and second elements, or None if the file is empty.
    """
    results = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # Skip header if needed (adjust if your CSV doesn't have a header)
        # next(reader, None)

        for row in reader:
            if row:  # Check if row is not empty
                # Split the row by semicolon

                split_row = row[0].split(';')
                first_element = split_row[0].strip()
                second_element = split_row[1].strip() if len(split_row) > 1 else ''
                results.append((first_element, second_element))

    return results


if __name__ == "__main__":
    # all_dfs = load_ontologies_classes()
    # write_ontologies_classes(df)

    # Example usage
    csv_file = './out/ontologies.csv'
    ontologies = read_csv_elements(csv_file)
    responses = []
    file = open(f"./out/results-gpt/results.md", "a")
    for index, ontology in enumerate(ontologies):
        prompt = str(ontology[0])
        if prompt != '' and prompt is not None:
            try:
                response = asyncio.run(run_gpt_stereotype_infer(user_prompt=prompt, filename=str(index)))
                responses.append((ontology[0], ontology[1], response))
                file.write(ontology[0] + ";" + ontology[1] + ";" + response + "\n")
            except Exception as e:
                print(e)
    file.close()

    # for index, df in enumerate(all_dfs):
    #     full_prompt = ""
    #     for item in df['name']:
    #         full_prompt = full_prompt + str(item) + ", "
    #     print(full_prompt)
    #     asyncio.run(run_local_stereotype_infer(user_prompt=full_prompt, filename=str(index)))
