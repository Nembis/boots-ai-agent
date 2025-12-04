import os

def get_files_info(working_directory, directory="."):
    try:
        full_working_path = os.path.abspath(working_directory)
        full_path = os.path.join(full_working_path, directory)
        if not full_path.startswith(full_working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        dirs = os.listdir(full_path)
        info_list = []
        for dir in dirs:
            full_dir = os.path.join(full_path, dir)
            file_size = os.path.getsize(full_dir)
            is_dir = not os.path.isfile(full_dir)
            info_list.append(f"\t- {dir}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(info_list)
    except Exception as e:
        return f"Error: {e}"


