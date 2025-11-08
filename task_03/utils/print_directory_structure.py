from colorama import Fore, init
from pathlib import Path

init(autoreset=True)


def print_directory_structure(path: Path, prefix:str = "") -> None:
    if not prefix:
       print(Fore.BLUE + path.name + "/") 
    
    children = sorted(list(path.iterdir()))

    for index, child in enumerate(children):
        is_last = index == len(children) - 1
        connector = "└── " if is_last else "├── "

        if (child.is_dir()):
            print(prefix + connector + Fore.BLUE + child.name + '/')

            new_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_structure(child, new_prefix)
        else:
            print(prefix + connector + Fore.GREEN + child.name)