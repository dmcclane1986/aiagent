import os

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
        
        # Security check: ensure target file is within working directory
        if not target_file.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if the target path is a regular file (this also checks existence)
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read only what we need to avoid loading huge files into memory
        with open(target_file, 'r', encoding='utf-8') as file:
            content = file.read(10001)  # Read one extra char to check if truncation needed
        
        # Truncate if longer than 10000 characters
        if len(content) > 10000:
            content = content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'
        
        return content
        
    except Exception as e:
        return f"Error: {str(e)}"