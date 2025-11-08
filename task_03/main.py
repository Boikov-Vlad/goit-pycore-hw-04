import sys
from pathlib import Path
from utils import print_directory_structure


def main():
    if len(sys.argv) < 2:
        print("Usage: python hw03.py <path_to_directory>")
        return
    
    path = Path(sys.argv[1])

    if not path.exists():
        print(f"Error: path does not exist: {path}")
        return
    
    if not path.is_dir():
        print(f"Error: path is not a directory: {path}")
        return
    
    print_directory_structure(path)

    
if __name__ == "__main__":
    main()
