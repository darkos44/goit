import re


grade = {'Oleg': 2,'Alex':3}
grade2 = {'Nasta': 5,'Sergey':4}
grade3 = {'Alex': 4,'Abdry':4}

result ={}

for x in (grade, grade2, grade3):
    result.update(x)

print(result)