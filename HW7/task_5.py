import os
import sys

size = {}


def scan_mem(path):
    for root, _, files in os.walk(path):
        for file in files:
            correct_file = os.path.join(root, file)
            mem = 10 ** (len(str(os.stat(correct_file).st_size)) - 1)
            file_extend = os.path.splitext(file)[-1]
            count, extends = size.get(mem, (0, set()))

            extends.add(file_extend)
            count += 1

            size[mem] = (count, extends)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        pth = sys.argv[1]
    else:
        pth = os.getcwd()

    scan_mem(pth)
    print({k: (v[0], list(v[1])) for k, v in size.items()})
