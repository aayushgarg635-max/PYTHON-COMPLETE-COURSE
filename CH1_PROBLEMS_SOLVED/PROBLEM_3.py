import os

# Define the target directory path ('.' represents your current working folder)
directory_path = "/"

try:
    # Fetch all files and folders in the target path
    directory_contents = os.listdir(directory_path)
    
    print(f"--- Contents of '{directory_path}' ---")
    
    # Iterate and print each individual entry item
    for item in directory_contents:
        print(item)
        
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: You do not have permission to access '{directory_path}'.")
