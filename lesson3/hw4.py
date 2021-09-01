import os
import sys
import easygui

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе

path = easygui.diropenbox(msg= "Choose directory")
#sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

types = {"image":('JPEG', 'PNG', 'JPG'),
        "video":('AVI', 'MP4', 'MOV'), 
        "doc":('DOC', 'DOCX', 'TXT'), 
        "music":('MP3', 'OGG', 'WAV', 'AMR'), 
        "desctop":('RDP')}

types_in_dir = set()

info_about_file = dict(zip(types.keys(), [list() for x in range(len(types))]))


for file in files:
    filename,file_extension  = os.path.splitext(file)
    file_extension = file_extension.upper()
    if file_extension == '':
        continue
    types_in_dir.add(file_extension)
    file_extension = file_extension[1:]
    for name_type, extension_type in types.items():
        if file_extension in extension_type:
            info_about_file[name_type].append(filename)
            break

 
print(*info_about_file.items())     
print(*types_in_dir)
input('Input enter to exit')

