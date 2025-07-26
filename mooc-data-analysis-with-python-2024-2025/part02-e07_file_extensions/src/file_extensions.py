#!/usr/bin/env python3

def file_extensions(filename):
    without_extension = []
    with_extension = {}

    with open(filename, 'r') as file:
        for line in file:
            file_name = line.strip()  
            if '.' not in file_name:
                without_extension.append(file_name.lstrip('.'))
            else:
                parts = file_name.split('.')
                extension= parts[-1]
                with_extension.setdefault(extension,[]).append(file_name)

    return (without_extension, with_extension)

def main():
    without_ext, with_ext = file_extensions("src/filenames.txt")
    print(f"{len(without_ext)} files with no extension")
    for extension in sorted(with_ext):
        print(f"{extension} {len(with_ext[extension])}")

if __name__ == "__main__":
    main()
