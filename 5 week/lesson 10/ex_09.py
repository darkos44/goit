import re

text = ''

result = re.findall(r'\b[a-zA-z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-z]{2,}', text)
print(result)

result = re.findall(r'\b[a-zA-z]{1}[\w\.]+@([a-zA-Z]+\.[a-zA-z]{2,})', text)
print(result)
