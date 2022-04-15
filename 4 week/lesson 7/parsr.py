from pathlib import Path

p = Path('.')

print(p.parent)
print(p.name)
print(p.suffix)
print(p.exists())
print(p.is_dir())
print(p.is_file())


def parse_folder(path):
    for el in path.iterdir():
       if el.is_dir():
           print(el.name)
           parse_folder(el)
       else:
            print(el.name) 

parse_folder(p)
