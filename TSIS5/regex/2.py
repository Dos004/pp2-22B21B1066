import re

with open(r"C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt", encoding='utf-8') as file:
    contents = file.read()
result = re.findall(".*a.*b.*b.*b?.*", contents)
print(result)
