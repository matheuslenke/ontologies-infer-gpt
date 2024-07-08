import json

import json.scanner
import pandas as pd
from src.parse_json import json_to_csv
from src.infer.gemini_infer import infer_stereotypes_gemini
from src.infer.openai_infer import infer_stereotype_openai
import pandas as pd
import json
import glob
from sklearn.metrics import accuracy_score, f1_score

def get_df():
    md_files = glob.glob('out/results-gemini/*.md')
    md_files.sort()
    all_data = []  # Create an empty list to store all the data
    for file in md_files:
        with open(file, 'r') as f:
            content = f.read().replace("```json\n", "").replace("```", "")
            if not content:
                continue
            try:
                data = json.loads(content)
                all_data.extend(data)  # Add the data to the list

                # df = pd.DataFrame(data)
                # print(df.describe())
                # df.to_csv('out/results-gemini/results.csv', index=False, mode="a", sep=";")
            except Exception as e:
                print(f"Error parsing file {file}")

    df = pd.DataFrame(all_data)  # Create a DataFrame from the list of data
    return df
    # df.to_csv('out/results-gemini/results.csv', index=False, mode="a", sep=";")

def calculate_metrics(combined_df):
    combined_df['inferred_stereotype'].fillna('None', inplace=True)
    combined_df['stereotype'].fillna('None', inplace=True)
    print(combined_df)
    combined_df.to_csv('out/results-gemini/combined.csv', sep=";", index=True)

    # Calculate the number of equal values in the columns
    equal_values = (combined_df['stereotype'] == combined_df['inferred_stereotype']).sum()

    print(f'Correctly inferred stereotypes: {equal_values}')
    # # Calculate the mean
    mean = equal_values / len(combined_df)
    print(f'Mean: {mean}')

    # # Calculate the accuracy
    accuracy = accuracy_score(combined_df['stereotype'], combined_df['inferred_stereotype'])
    print(f'Accuracy: {accuracy}')
    # # Calculate the f1-score
    f1 = f1_score(combined_df['stereotype'], combined_df['inferred_stereotype'], average='weighted')
    print(f'F1-score: {f1}')

def combine_dfs():
    df = pd.read_csv("./out/results-gemini/results.csv", sep=";")
    original_df = pd.read_csv('classes.csv', sep=";")
    df.sort_values(by=['name'], inplace=True)
    df.drop_duplicates(subset=['name'], keep='first', inplace=True)

    original_df.sort_values(by=['name'], inplace=True)
    original_df = original_df[['name', 'stereotype', 'number']]
    original_df.drop_duplicates(subset=['name'], keep='first', inplace=True)

    return original_df.merge(df, sort=True, how="left")

if __name__ == "__main__":
    # infer_stereotypes_gemini()
    # After ending...
    json_to_csv()
    combined_df = combine_dfs()
    calculate_metrics(combined_df)
    combined_df.to_csv('out/results-gemini/combined.csv', sep=";", index=False)

    # infer_stereotype_openai(model="mistral")


    # responses = []
    # file = open(f"./out/results-gpt/results.md", "a")
    # for index, ontology in enumerate(ontologies):
    #     prompt = str(ontology[0])
    #     if prompt != '' and prompt is not None:
    #         try:
    #             response = asyncio.run(run_gpt_stereotype_infer(user_prompt=prompt, filename=str(index)))
    #             responses.append((ontology[0], ontology[1], response))
    #             file.write(ontology[0] + ";" + ontology[1] + ";" + response + "\n")
    #         except Exception as e:
    #             print(e)
    # file.close()

    # for index, df in enumerate(all_dfs):
    #     full_prompt = ""
    #     for item in df['name']:
    #         full_prompt = full_prompt + str(item) + ", "
    #     print(full_prompt)
    #     asyncio.run(run_local_stereotype_infer(user_prompt=full_prompt, filename=str(index)))
