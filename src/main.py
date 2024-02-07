from openai import OpenAI
import os
from prompt_messages import delimiter, ufo_explanation, stereotypes_explanation, instructions

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

client = OpenAI()
client.api_key  = os.getenv('OPENAI_API_KEY')

### This function gets a completion from ChatGPT API based on a Prompt
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": ufo_explanation},
        {"role": "system", "content": stereotypes_explanation},
        {"role": "system", "content": instructions},
        {"role": "user", "content": f"{delimiter} {prompt} {delimiter}"}
        ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message

def get_knowledge_files():
    file = client.files.create(
        file=open("knowledge.pdf", "rb"),
        purpose="assistants"
    )

# Output to a MD file for better readability
def output_to_file(prompt, message, filename = "out.md"):
    folder_path = "out"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Prompt\n\n")
        file.write(prompt)
        file.write("\n\n # Response\n\n")
        file.write(message)


# This function executes a user prompt calling OpenAI GPT API and with the instructions provided to infer types
def run_gpt_stereotype_infer():
    user_prompt="Please provide to me a model with 20 elements related to Robert Alexy Law theory, infering stereotypes. Try to give as many different stereotypes as you can"
    response = get_completion(user_prompt)

    print(response.content)
    output_to_file(user_prompt, response.content, filename="output2.md")


if __name__ == "__main__":
    run_gpt_stereotype_infer()