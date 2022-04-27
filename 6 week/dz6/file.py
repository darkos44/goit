import sys
import pathlib

files_extension = {
        'audio':{'MP3', 'OGG', 'WAV', 'AMR'},
        'video':{'AVI', 'MP4', 'MOV', 'MKV'},
        'documents':{'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'},
        'images':{'JPEG', 'PNG', 'JPG', 'SVG'},
        'archives':{'ZIP', 'GZ', 'TAR'},
        'etc':{},
    }

def sorted_files(path: pathlib.Path, files:dict[list]):
    for el in path.iterdir():
       if el.is_dir():
           sorted_files(el, files)
       else:
            file_extension = el.suffix()
            for name, extension in files_extension.items():
               if  file_extension.upper() in extension:
                   files[name].append(el.name)
                   break
            else:
                files['etc'].append(el.name)
                global files_extension
                files_extension['etc'].add(file_extension.upper())


def create_dir(path: pathlib.Path, files:dict[list]):
    for name_dir in files.keys():
        new_Path = pathlib.Path(path.home(), name_dir)
        if not new_Path.exists():
            pathlib.Path.mkdir(path.home(), name_dir)


def main():
    str_path = sys.argv[1]
    files = {
        'audio':[],
        'video':[],
        'documents':[],
        'images':[],
        'archives':[],
        'etc':[],
    }
    Path = pathlib.Path(str_path)
    create_dir(Path, files)
    sorted_files(Path, files)
    print(files)


if __name__ == "__main__":
    main()
