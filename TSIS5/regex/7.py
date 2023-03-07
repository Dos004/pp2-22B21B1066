import re
with open(r'C:\Users\diase\OneDrive\Рабочий стол\Python\PP2\row.txt',encoding='utf-8') as file:
    content= file.read()
    # red_mad_robot - snake case
    # redMadRobot - camel case
result=re.sub(r"(?:^|_)([a-z])",lambda match:match.group(1).upper(),content) 
#(?:^|_)- group(0)
#([a-z])- group(1)
print(result) 