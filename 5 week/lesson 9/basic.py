# print('Test. \nNew string')
# print('Test.\tNew string')
# print('Test. New string', end='\n\r')
# print('Test. Hello world', end='\r')
# print('Test. AAAAAAAAA', end='')


# string = 'Исключить из этой [строка группы]'
# start_index = string.find('[')
# end_index = string.find(']')
# new_string = string[:start_index] + string[end_index + 1:]
# print(new_string)
# def sanitize(string):
#     new_string = string[]
#     while True:
#         start_index = new_string.find('[')
#         end_index = new_string.find(']')
#         if start_index == -1:
#             break
#         new_string = new_string[:new_string] + new_string[end_index + 1:]
#     return new_string
# print(sanitize(string))


# isdigit()
# print('3'.isdigit())


# def count_digit(string:str):
#     count = 0
#     for x in string:
#         if x.isdigit():
#             count += 1
#     return count

# print(count_digit("Name 56 8962"))


# def count_number(string:str):
#     count = 0
#     pos = 0
#     nums = []
#     while pos < len(string):       
#         if string[pos].isdigit():
#             num = ''
#             while pos < len(string) and string[pos].isdigit():
#                 num = num + string[pos]
#                 pos += 1
#             count += 1
#             nums.append(num)
#         else:
#             pos += 1
#     return count, nums

# print(count_number("Name 56 8962"))

# numbers = ['123', '456', '789', '321', '18', '75', 'abc', '23c']

# def sanitize(data:list[str]) -> list:
#     res = []
#     for x in data:
#         if x.isdigit():
#             res.append(int(x))
#     return res

# sum_numbers = sanitize(numbers)
# sum_numbers.sort()
# print(sum_numbers)
# print(max(sum_numbers) - min(sum_numbers))
# print(min(sum_numbers) / len(sum_numbers))


# string = 'У меня была собака поп ее убил'
# slova = string.split(' ')
# print(slova)
# print('.'.join(slova))


# url = ''
# _, query = url.split('?')

# obj_query = {}
# for x in query.split('&'):
#     key, value = x.split('=')
#     obj_query.update(key, value.replace('+',''))

# prepere = []
# for key in obj_query:
#     prepere.append(key + '='+obj_query[key])
# print(';'.join(prepere))

phone_storage = ['380508892081', '   + 3 8 0 50 4558662']

codes_operators = ['050']

def is_valid_operator(phone: str) -> bool:
    if phone[:3] in codes_operators:
        return True
    return False


def sunityze(phone: str) -> str:
    new_phone = phone.strip().removeprefix('+').replace('(','').replace(')','').replace(' ','').replace('-','')
    return new_phone


def is_valid_phone(phone: str) -> bool:
    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] =='38':
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


if __name__ == "__main__":
    for phone in phone_storage:
        phone = sunityze(phone)
        is_valid = is_valid_phone(phone)
        if is_valid:
            print("Phone {:^16} is valid".format(phone))
        else:
            print("Phone {:^16} is not valid".format(phone))


# registration = []

# connect = []


# if __name__ == "__main__":
#     valid_regidtration = []
#     for phone in registration:
#         if is_valid_phone(phone):
#             valid_regidtration.append(phone)
#     valid_connect = []
#     for phone in connect:
#         if is_valid_phone(phone):
#             valid_connect.append(phone)

#     result = set(valid_regidtration) & set(valid_connect)
#     print(result)

# map = {ord('с'):'s',ord('ю'):'y',ord('я'):'ya',ord('ш'):'sh',}

# translate = 'Юля шла а я бежал. Скоро шторм'.translate(map)
# print(translate)


# symbols = ['1']
# code = ['0000']


# map = {}
# for key, value in zip(symbols, code):
#     map.update(ord(key),code)
#     map.update(ord(key.lower()),code)

# result = '36 BF 55 CA'.translate(map)
# print(result)
