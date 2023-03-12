import os

tsis6 = os.path.join(os.getcwd(),'TSIS6')

os.chdir(tsis6)

for i in range(97,122):
    name = chr(i) + '.txt'
    with open(name, 'w') as f:
        f.write(" ")