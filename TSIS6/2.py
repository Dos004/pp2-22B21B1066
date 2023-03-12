import os

path = os.getcwd() 


if os.path.exists(path):
    print(f"The path {path} exists.")

    if os.access(path, os.R_OK):
        print(f"The path {path} is readable.")
    else:
        print(f"The path {path} is not readable.")

    if os.access(path, os.W_OK):
        print(f"The path {path} is writable.")
    else:
        print(f"The path {path} is not writable.")

    if os.access(path, os.X_OK):
        print(f"The path {path} is executable.")
    else:
        print(f"The path {path} is not executable.")
else:
    print(f"The path {path} does not exist.")