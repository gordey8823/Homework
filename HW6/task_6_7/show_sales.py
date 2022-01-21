import sys


def show_sales(argv):
    if len(argv[1:]) == 0:

        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            line = fr.readline()
            while line:
                print(line.strip())
                line = fr.readline()

    elif len(argv[1:]) == 1:

        start_line = int(argv[1])
        count = 0
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            while start_line != count:
                line = fr.readline()
                count += 1
            else:
                while line:
                    print(line.strip())
                    line = fr.readline()

    elif len(argv[1:]) == 2:

        start_line, stop_line = int(argv[1]), int(argv[2])
        count = 0
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            line = fr.readline()
            while line:
                if start_line-1 <= count < stop_line:
                    print(line.strip())
                line = fr.readline()
                count += 1


if __name__ == '__main__':
    exit(show_sales(sys.argv))
