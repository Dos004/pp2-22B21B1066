import re


with open(file="row.txt",mode='r',encoding='UTF-8') as f:
    l = len(re.findall('\n',f.read()))
print(l+1)