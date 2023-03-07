import re
string= 'redMadRobot'

result = re.sub(r'(?<!^)(?=[A-Z])','_',string).lower()
print(result)
    # redMadRobot - camel case
    # red_mad_robot - snake case