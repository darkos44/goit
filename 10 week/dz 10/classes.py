from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, name:str):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)




class Record:
    def __init__(self, name: str, adr=''):
        self.Name = Name(name)
        self.Phones = []
        if adr != '':
            self.add_address(adr)

    def add_address(self, adr: str):
        self.Phones.append(Phone(adr))

    def delete_address(self, adr: str):
        for i in range(len(self.Phones)):
            self.Phones.pop()

    def get_phone(self):
        result = ""
        for phone in self.Phones:
            if result != '':
                result += ', '
            result += phone.value
        return result

    def change_addres(self, adr: str):
        for i in range(len(self.Phones)):
            if self.Phones[i].value == adr:
                self.Phones[i].value = adr
                break


class AddressBook(UserDict):
    def __init__(self, *args):
        super().__init__(*args)

    def add_record(self, record: Record):
        self.data[record.Name.value] = record

    def find_record(self, name):
        return self.data.get(name, 1)

    def show_all(self):
        result = ''
        for k, v in self.data.items():
            result += f'{k}: ' + v.get_phone() + '\n'
        return result

