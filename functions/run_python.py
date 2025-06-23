import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
        
        # Security check: ensure target file is within working directory
        if not target_file.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if file is a Python file (also implicitly checks existence when combined with isfile)
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Check if file exists and is a regular file
        if not os.path.isfile(target_file):
            return f'Error: File "{file_path}" not found.'
        
        # Execute the Python file
        result = subprocess.run(
            ['python', target_file],
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Build output efficiently
        output_parts = []
        
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        return '\n'.join(output_parts) if output_parts else "No output produced."
        
    except subprocess.TimeoutExpired:
        return "Error: executing Python file: Process timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"