import re

text = ''
phones = []

pattern = r'\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}'

for phone in phones:
    print(f'{phone} is valid: {re.match(pattern, phone)}')