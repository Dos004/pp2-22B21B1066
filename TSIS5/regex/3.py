#class code
import re

with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding='utf-8') as file:
    content = file.read()
result = re.findall("[a-z]+_[a-z]+",content)
print(result)
import re
#my code
with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
    contents = file.read()
result = re.findall(r'[A-Z]?[a-z]+_[a-z]+',contents)
print(result)