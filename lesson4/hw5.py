import os
import sys
import easygui


def initialization_array_of_types():
    return {"image":('JPEG', 'PNG', 'JPG'),
        "video":('AVI', 'MP4', 'MOV'), 
        "doc":('DOC', 'DOCX', 'TXT'), 
        "music":('MP3', 'OGG', 'WAV', 'AMR'), 
        "desctop":('RDP'),
        "archive": ('ZIP', 'GZ', 'TAR'),}


def get_info_about_file(types_array, path):
    files = os.listdir(path)
    unknown_types = set()
    known_types = set()
    info_about_file = dict(zip(types_array.keys(), [list() for x in range(len(types_array))]))
    for file in files:
        filename,file_extension  = os.path.splitext(file)
        file_extension = file_extension.upper()
        if file_extension == '':
           get_info_about_file(types_array, path + os.sep + filename)      
        file_extension = file_extension[1:]
        for name_type, extension_type in types_array.items():
            if file_extension in extension_type:
                info_about_file[name_type].append(filename)
                known_types.add(file_extension)
                break
        else:
            unknown_types.add(file_extension) 



def main():
    types_array = initialization_array_of_types()
    path = easygui.diropenbox(msg= "Choose directory")
    #sys.argv[1]
    print(f"Start in {path}")

