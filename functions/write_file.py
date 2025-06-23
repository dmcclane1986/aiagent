import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
        
        # Security check: ensure target file is within working directory
        if not target_file.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Create directory if it doesn't exist (exist_ok=True prevents error if dir exists)
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        
        # Write content to file
        with open(target_file, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {str(e)}"