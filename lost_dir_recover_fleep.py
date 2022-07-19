#!/usr/bin/env python3

import fleep
import argparse
import shutil
import pathlib

def createArgParser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument ("-s" ,"--source", dest="source", \
                        required=True, help="Source directory with files (LOST.DIR)")
    parser.add_argument ("-d" , "--destination", dest="destination", \
                        required=True, help="The folder to which the files will be copied")
    parser.add_argument ("-q", "--quiet", dest="quiet", required=False, \
                        default=False, action="store_true")
    return parser
    
def start_recover(args):
    cwd = pathlib.Path.cwd()
    
    # Просматриваем папку с файлами, которым нужно добавить расширение
    for child in (cwd / args.source).iterdir():
        # Скипаем если это не файл
        if not child.is_file():
            if not args.quiet:
                print("[-] Skip", child.name, ", is not a file")
            continue
        # Скипаем если это ссылка
        if child.is_symlink():
            if not args.quiet:
                print("[-] Skip", child.name, ", is a symlink")
            continue
        
        # Открываем файл и читаем из него первые 128 байт, больше библиотеке fleep и не нужно
        with open(child, "rb") as file:
            info = fleep.get(file.read(128))
        
        new_dir_name = ""
        
        # В случае если тип файла не определяется (часто из за мусора после востановления из LOST.DIR)
        # Кидаем файлы в папку неизвестное
        if len(info.extension) == 0:
            new_extension = "unknown"
        else:
            new_extension = info.extension[0]
        
        # Пытаемся создать новый каталог внутри переданного пользователем каталоге
        (cwd / args.destination / new_extension).mkdir(parents=True, exist_ok=True)
        
        new_name = child.name + "." + new_extension
        
        # Копируем старый файл с новым расширением
        shutil.copy(child, cwd / args.destination / new_extension / new_name)
        
        if not args.quiet:
            print("[+]", new_extension, "|", new_name)


if __name__== "__main__":
    parser = createArgParser()
    arguments = parser.parse_args()
    
    start_recover(arguments)
    
