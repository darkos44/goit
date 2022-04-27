import re

text = ''

result = re.findall(r'https?://\w{3,}\.?(?:\w\.)*\w{2,5}', text)
print(result)