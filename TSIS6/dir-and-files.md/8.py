import os

path = "path/to/file"

if os.path.exists(path):
    
    if os.access(path, os.R_OK):
        os.remove(path)
        print(f"{path} has been deleted")
    else:
        print(f"You don't have access to {path}")
else:
    print(f"{path} does not exist")
