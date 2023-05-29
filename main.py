from function import make_dir, sort_files, check
import sys


def main():
    path = sys.argv[1]
    if make_dir(path):
        sort_files(path, path)
        check(path)


if __name__ == '__main__':
    main()
