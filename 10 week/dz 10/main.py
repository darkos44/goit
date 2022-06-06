from classes import AddressBook, Record, Name, Phone

CONTACT = AddressBook()


def main():
    say = input("Enter command:")
    exit_frase = (
        'good bye',
        'close',
        'exit',
        '.',
    )
    while not say.lower() in exit_frase:
        command = say.split(' ')
        if len(command) == 0:
            print('You entered nothing')
            say = input("Enter command: ")
            continue
        func_name = command[0]
        phone_str = ''
        name_str = ''
        try:
            if func_name.lower() != 'show' and func_name.lower() != 'hello':
                name_str = command[1]
            if func_name.lower() == 'add' or func_name.lower() == 'change':
                phone_str = command[2]
            if func_name.lower() == 'show' and len(command) >= 2:
                func_name = func_name + ' ' + command[1]
        except IndexError:
            print('Give me name and/or phone please')
            say = input("Enter command: ")
            continue
        if func_name == 'hello':
           print('How can I help you?')
        elif func_name == 'add':
            name = Name(name_str)
            phone = Phone(phone_str)
            record = Record(name, phone)
            CONTACT.add_record(record)
        elif func_name == 'change':
            record = CONTACT.find_record(name_str)
            if record != 1:
                record.delete_address(phone_str)
                phone = Phone(phone_str)
                record.add_address(phone)
        elif func_name == 'phone':
            record = CONTACT.find_record(name_str)
            if record != 1:
                print(record.get_phone())
            else:
                print('This name have no phone')
        elif func_name == 'show all':
            print(CONTACT.show_all())
        else:
            print("Function does not exist")
        say = input("Enter command: ")




if __name__ == '__main__':
    main()