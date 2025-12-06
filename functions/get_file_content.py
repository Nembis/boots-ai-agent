import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        full_working_dir = os.path.abspath(working_directory)
        full_file_dir = os.path.abspath(os.path.join(full_working_dir, file_path))
        if not full_file_dir.startswith(full_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_file_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_file_dir, "r") as f:
            file_content = f.read(MAX_CHARS)
        if len(file_content) == MAX_CHARS:
            file_content += f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content
    except Exception as e:
        return f"Error: {e}"
