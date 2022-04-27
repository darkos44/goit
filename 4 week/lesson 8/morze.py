from unittest import result


morze_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
              'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
              'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
              'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
              'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
              '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
              '8':'---..', '9':'----.'}


def convert_world_to_morze(text: str) ->str:
    result = ''
    text = text.upper()
    for ch in text:
        #result += morze_dict.setdefault(ch,'')
        #if ch in morze_dict:
           result += morze_dict.get(ch,'') 
    return result

def main():
    text = input('Введите строку для кодировки ')
    while text != '':
        print(f'Ваша строка в морзе выглядит так {convert_world_to_morze(text)}')
        text = input('Введите строку для кодировки ')


if __name__ == '__main__':
    main()