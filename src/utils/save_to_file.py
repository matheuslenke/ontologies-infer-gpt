def save_to_file(file_path: str, content: str):
    '''
    Save any content to a file with Append mode
    '''
    with open(file_path, "a") as result_file:
         result_file.write(content)