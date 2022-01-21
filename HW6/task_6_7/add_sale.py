import sys
def main(argv):
    program, argv1 = argv
    with open('bakery.csv', 'a', encoding='utf-8') as aw:
        aw.write(argv[1] + '\n')

if __name__ == "__main__":
    exit(main(sys.argv))
    