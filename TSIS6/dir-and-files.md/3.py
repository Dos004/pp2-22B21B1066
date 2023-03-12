import os
path = os.getcwd()

if os.path.exists(path):
    file_dir = os.listdir(path)
    for i in file_dir:
        if os.path.isfile(os.path.join(path,i)):
            print(i)
        else:
            continue
else:
    print("path does'nt exists")
