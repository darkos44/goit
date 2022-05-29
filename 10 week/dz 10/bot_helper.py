CONTACT = dict()


def input_error(func):
    def inner(*args, **kvards):
        try:
            result = func(*args, **kvards)
        except KeyError:
            print('Enter user name')
        except IndexError:
            print('Give me name and/or phone please')
        return result
    return inner


@input_error
def hello_func(name, phone) -> str:
    return 'How can I help you?'


@input_error
def add_func(name, phone) -> str:
    CONTACT[name] = phone
    return f'Contact {name} is added'


@input_error
def change_func(name, phone) -> str:
    CONTACT[name] = phone
    return f'Contact {name} is change'


@input_error
def phone_func(name, phone) -> str:
    return CONTACT.get(name, 'This name have no phone')


@input_error
def show_func(name, phone) -> str:

    result = ''
    for k, v in CONTACT.items():
        result = result + f'{k}: {v}\n'
    return result


FUNC_DICT = {
    'hello': hello_func,
    'add': add_func,
    'change': change_func,
    'phone': phone_func,
    'show all': show_func,

}


def main():
    say = input("Enter command:\n")
    exit_frase = (
        'good bye',
        'close',
        'exit',
        '.',
    )
    while True:
        if say.lower() in exit_frase:
            break
        command = say.split(' ')
        if len(command) == 0:
            print('You entered nothing')
            say = input("Enter command: ")
            continue
        func_name = command[0]
        phone = ''
        name = ''
        try:
            if func_name.lower() != 'show' and func_name.lower() != 'hello':
                name = command[1]
            elif func_name.lower() == 'add' or func_name.lower() == 'change':
                phone = command[2]
            elif func_name.lower() == 'show' and len(command) >= 2:
                func_name = func_name + ' ' + command[1]
        except IndexError:
            print('Give me name and/or phone please')
            continue

        try:
            func = FUNC_DICT[func_name.lower()]
        except KeyError:
            print("Function does not exist")
            say = input("Enter command: ")
            continue
        result = func(name, phone)
        print(result)
        say = input("Enter command: ")
    else:
        print('Good bye!')


if __name__ == '__main__':
    main()