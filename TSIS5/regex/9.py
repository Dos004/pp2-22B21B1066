import re
with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding='utf-8')as file:
    content = file.read()
string = 'LetUsBigFast'
result = re.findall(r'[A-Z][a-z]*',content)
print('_'.join(result),sep='\n')
result = re.findall(r'[A-Z][a-z]*',string)
print('_'.join(result),sep='\n')