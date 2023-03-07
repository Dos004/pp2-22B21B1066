import re

txt = "The rain in Spain"
y = re.search("^The.*Spain$", txt)
print(y)