# import re

# with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
#     contents = file.read()
# result = re.findall(r'.*a.*b{0,} ',contents)
# print(result)

# 2
# import re

# with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
#     contents = file.read()
# result = re.findall(r'.*a.*b.*b.*b?.*',contents)
# print(result)

#3
# import re

# with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
#     contents = file.read()
# result = re.findall(r'[A-Z]?[a-z]+_[a-z]+.*',contents)
# print(result)
#4
# import re

# with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
#     contents = file.read()
# result = re.findall(r'^[A-Z][a-z]+',contents)
# print(result)

#5
# import re
# with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
#     contents = file.read()
# result = re.findall(r'.*a.*b$',contents)
# print(result)

#6
# import re
# with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding="utf-8") as file:
#     contents = file.read()
# result = re.sub(r'[ ,.]',r':',contents)
# print(result)
import re

camel_case_str = "HelloWorld"

# Разделить строку на заглавные буквы с помощью регулярного выражения
snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()

print(snake_case_str)  # "hello_world"