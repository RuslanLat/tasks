import os
import sys
import argparse
from os.path import join, getsize, basename


def createParser():
    parser = argparse.ArgumentParser(
        description="Вывод структуры папки (в виде дерева)", add_help=False
    )
    parser.add_argument(
        "-p",
        "--path",
        default=os.getcwd(),
        help="путь к папке (по умолчанию текущая папка)",
    )
    parser.add_argument(
        "-h",
        "--help",
        "-help",
        action="help",
        help="для вывода структуры папки (в виде дерева) необходимо указать путь к папке",
    )
    return parser


def dfs_tree(path):
    def tree(path, level):
        dsize, files, dirs = 0, [], []
        # формирование структуры папки (в виде дерева)
        files.append(f'{" " * (level - 1) * 4}\\{basename(path)}\\ ')
        # перебор в цикле всех файлов и папок в отсортированном списке (сначала папки, потом файлы)
        for item in sorted(
            os.listdir(path), key=lambda x: os.path.isfile(join(path, x))
        ):
            # путь к файлу или папке
            fullname = join(path, item)
            # условие если это папка
            if os.path.isdir(fullname):
                # рекурсивный вызов функции
                tmp = tree(fullname, level + 1)
                # подсчет размера папки
                dsize += tmp[0]
                # формирование структуры папки
                files.append(tmp[1])
            # условие если это файл
            else:
                # размер файла
                fsz = getsize(fullname)
                # формирование структуры папки (в виде дерева)
                files.append(f'{" " * level * 4}{item}  [{fsz:,} bytes]')
                # подсчет размера папки
                dsize += fsz
        # формирование структуры папки (в виде дерева)
        files[0] += f"[{dsize:,} bytes]"

        return dsize, "\n".join(files)

    return tree(path, 1)[1]


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.path:
        print(dfs_tree(namespace.path))
    elif namespace.help:
        print("Это help")
