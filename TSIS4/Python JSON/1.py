import json
x = '{"name": "John","age":"36","city":"New York"}'

y = json.loads(x)
print(y['age'])