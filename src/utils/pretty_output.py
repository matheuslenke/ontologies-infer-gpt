# Output to a MD file for better readability
import os


def output_to_file(prompt, message, filename = "out.md"):
    folder_path = "out"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Prompt\n\n")
        file.write(prompt)
        file.write("\n\n # Response\n\n")
        file.write(message)
