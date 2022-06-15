from collections import UserDict
from datetime import datetime
import pickle


class Field:
    def __init__(self, value) -> None:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    @Field.value.setter
    def value(self, name: str):
        self._value = name


class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)

    @Field.value.setter
    def value(self, new_value: str):
        if not new_value.isdigit():
            print('Phone must be digit')
        else:
            self._value = new_value


class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        try:
            d, m, y = new_value.split('-')
            date = datetime(day=int(d), month=int(m), year=int(y))
            self._value = date
        except ValueError:
            print('Enter date like 02-05-2022')


class Record:
    def __init__(self, name: Name, adr: Phone, birthday=None):
        self.Name = name
        self.Birthday = birthday
        self.Phones = []
        if adr != '':
            self.add_address(adr)

    def add_address(self, adr: Phone):
        self.Phones.append(adr)

    def delete_address(self, adr: Phone):
        for p in self.phones:
            if p.value == adr.value:
                self.phones.remove(p)
                return p

    def get_phone(self):
        result = ""
        for phone in self.Phones:
            if result != '':
                result += ', '
            result += phone.value
        return result

    def change_address(self, adr: str):
        for i in range(len(self.Phones)):
            if self.Phones[i].value == adr:
                self.Phones[i].value = adr
                break

    def days_to_birthday(self):
        if self.Birthday is None:
            return 'Birthday day not set'
        date_now = datetime.now()
        birthday_date = datetime(year=date_now.year, month=self.Birthday.value.month, day=self.Birthday.value.day)
        if date_now > birthday_date:
            birthday_date = datetime(year=date_now.year + 1, month=self.Birthday.value.month,
                                     day=self.Birthday.value.day)
        result = birthday_date - date_now
        return result.days


class AddressBook(UserDict):
    def __init__(self, *args):
        super().__init__(*args)
        self.count = 0
        self.load_data()

    def add_record(self, record: Record):
        self.data[record.Name.value] = record

    def find_record(self, name):
        return self.data.get(name, 1)

    def show_all(self):
        result = ''
        for k, v in self.data.items():
            result += f'{k}: ' + v.get_phone()
            if not v.Birthday is None:
                result += f' birthday {v.Birthday.value}'
            result += '\n'
        return result

    def iterator(self, n=2):
        key_list = list(self.data.keys())
        if self.count + 1 >= len(key_list):
            self.count = 0
            return None
        result_list = key_list[self.count: min(self.count + n, len(key_list))]
        result = ''
        for k in result_list:
            result += f'{k}: ' + self.data[k].get_phone()
            if not self.data[k].Birthday is None:
                result += f' birthday {self.data[k].Birthday.value}'
            result += '\n'
            self.count += 1
        yield result

    def save_data(self):
        with open('data.bin', 'wb') as f:
            pickle.dump(self.data, f)

    def load_data(self):
        try:
            with open('data.bin', 'rb') as f:
                try:
                    data = pickle.load(f)
                    self.data = data
                except EOFError:
                    print('File data is empty')
        except FileNotFoundError:
            print('File data is empty')

    def find_all(self, value):
        result = ''
        for k, v in self.data.items():
            found = False
            if k.find(value) != -1:
                found = True
            for phone in v.Phones:
                if phone.value.find(value) != -1:
                    found = True
            if found:
                result += f'{k}: ' + v.get_phone()
                if not v.Birthday is None:
                    result += f' birthday {v.Birthday.value}'
                result += '\n'
        return result
