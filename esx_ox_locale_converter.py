import os
import re

def process_file(input_file_path, output_file_path):
    """
    Converts a single ESX FiveM locale file from .lua format to JSON format.

    Args:
        input_file_path (str): The path to the input .lua file.
        output_file_path (str): The path to the output .json file.
    """
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()

    output_lines = []
    
    for line in lines:
        match = re.match(r'\s*\["(.*?)"\]\s*=\s*"([^"]*)",?\s*', line)
        if match:
            key, value = match.groups()
            output_lines.append(f'    "{key}": "{value}"')

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("{\n")
        if output_lines:
            output_file.write(",\n".join(output_lines))
        output_file.write("\n}")

def process_files_in_directory(input_directory, output_directory):
    """
    Processes all .lua files in a directory, converting them to .json format.

    Args:
        input_directory (str): The path to the directory containing .lua files.
        output_directory (str): The path to the directory where .json files will be saved.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".lua"):
            output_filename = filename.replace(".lua", ".json")
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, output_filename)
            process_file(input_file_path, output_file_path)
            print(f"Processed {filename}")

if __name__ == "__main__":
    cwd = os.getcwd()

    input_directory = os.path.join(cwd, "locales")
    output_directory = os.path.join(input_directory, "ox_output")
    process_files_in_directory(input_directory, output_directory)
