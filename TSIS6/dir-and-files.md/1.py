import os
listdir = []
listfile = []

path=os.getcwd()

files_and_dirs  = os.listdir(path)

for i in files_and_dirs:
    if os.path.isdir(os.path.join(path,i)):
        listdir.append(i)

    else:
        listfile.append(i)

print(listdir)

print(listfile)

