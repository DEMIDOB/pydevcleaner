import os
import shutil
import sys


def clean_venvs(path):
    for dir in os.listdir(path):
        new_path = os.path.join(path, dir)
        if not os.path.isdir(new_path):
            continue

        if dir in {'venv', '.venv'}:
            shutil.rmtree(new_path)
            print(f"Removing {new_path}")
        else:
            clean_venvs(new_path)


def _main():
    argv = sys.argv
    if not os.path.isdir(argv[-1]):
        print("The last argument passed to the command line should be the target directory!")
        return

    ans = input(f'Do you want to clean {argv[-1]}? ("y" for yes)')
    if ans.lower() != "y":
        return

    clean_venvs(argv[-1])


if __name__ == "__main__":
    _main()