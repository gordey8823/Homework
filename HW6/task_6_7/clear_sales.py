import sys


def clear_file(argv):
    with open('bakery.csv', 'w+', encoding='utf-8') as fr:
        fr.write('')


if __name__ == '__main__':
    exit(clear_file(sys.argv))
