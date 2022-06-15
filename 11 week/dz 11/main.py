from classes import AddressBook, Record, Name, Phone, Birthday
from datetime import datetime

CONTACT = AddressBook()


def main():
    say = input("Enter command: ")
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
        func_name = command[0].lower()
        phone_str = ''
        name_str = ''
        try:
            if func_name != 'show' and func_name != 'hello':
                name_str = command[1]
            if func_name == 'add' or func_name == 'change' or func_name == 'add_p' or func_name == 'add_b':
                phone_str = command[2]
        except IndexError:
            print('Give me name and/or phone please')
            say = input("Enter command: ")
            continue

        if func_name == 'hello':
           print('How can I help you?')
        elif func_name == 'add':
            name = Name(name_str)
            phone = Phone(phone_str)
            birthday = None
            if len(command) == 4:
                birthday = Birthday(command[3])
            record = Record(name, phone, birthday)
            CONTACT.add_record(record)
        elif func_name == 'add_b':
            record = CONTACT.find_record(name_str)
            if record != 1:
                birthday = Birthday(phone_str)
                record.Birthday = birthday
        elif func_name == 'add_p':
            record = CONTACT.find_record(name_str)
            if record != 1:
                phone = Phone(phone_str)
                record.add_address(phone)
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
        elif func_name == 'days_to_birthday':
            record = CONTACT.find_record(name_str)
            if record != 1:
                print(record.days_to_birthday())
        elif func_name == 'show':
            func2 = command[1]
            if func2 == 'all':
                print(CONTACT.show_all())
            else:
                num = 2
                try:
                    num = int(func2)
                except:
                    print('Enter integer')
                iterator = CONTACT.iterator(num)
                for x in iterator:
                    print(x)

        else:
            print("Function does not exist")
        say = input("Enter command: ")


if __name__ == '__main__':
    main()