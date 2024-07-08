import json
import glob

from src.utils.save_to_file import save_to_file
import pandas as pd

class InferResult:
    def __init__(self, name: str, stereotype: str, explanation: str):
        self.name = name
        self.stereotype = stereotype
        self.explanation = explanation

    def __str__(self):
        return f"{self.name};{self.stereotype};{self.explanation}"

    def __repr__(self):
        return self.__str__()

def parse_json_from_file(file_path: str) -> pd.DataFrame:
    with open(file_path, "r") as file:
        json_str = ""
        found_json = False
        for line in file:
            if line.strip() == "```json" and not found_json:
                found_json = True
            elif line.strip() == "```" and found_json:
                break
            elif not found_json:
                continue
            elif found_json:
                json_str += line

        parsed_json = json.loads(json_str)
        df = pd.DataFrame(parsed_json)
        return df
    

def json_to_csv():
    file_paths = glob.glob("out/results-gemini/*.md")
    for file_path in file_paths:
        try:
            df = parse_json_from_file(file_path)
            # Process the JSON data and convert it to CSV format
            # Save the CSV file
            csv_string = ""
            csv_string = df.to_csv(index=False, sep=";")


            save_to_file("out/results-gemini/results.csv", csv_string)
        except Exception as e:
            print(f'Error in file {file_path}')
            continue