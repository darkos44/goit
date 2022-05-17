def sequence_buttons(string):
    CYRILLIC = ('.', ',', '?', '!', ':', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
    LATIN = ('1', '11', '111', '1111', '11111', '2', '22', '222',
             '3', '33', '333',
             '4', '44', '444',
             '5', '55', '555',
             '6', '66', '666',
             '7', '77', '777', '7777',
             '8', '88', '888',
             '9', '99', '999', '9999', '0')

    TRANSLIT_DICT = {}

    for c, l in zip(CYRILLIC, LATIN):
        TRANSLIT_DICT[ord(c)] = l
        TRANSLIT_DICT[ord(c.upper())] = l.upper()
    s = string.translate(TRANSLIT_DICT)
    print(s)
    return s