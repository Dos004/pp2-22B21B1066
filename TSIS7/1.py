import os

print(os.getcwd())
tsis7=os.path.join(os.getcwd(),"TSIS7")
os.chdir(tsis7)
print(os.getcwd())

for i in range(2,11):
    name = str(i) + ".py"
    with open(name,"w") as file:
        file.write(" ")


