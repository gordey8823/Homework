from sys import argv
from utils import currency_rates_adv

def main(argv):
    kurs, date_value = currency_rates_adv(argv[1])
    print(f'{kurs} {date_value}')



if __name__ == '__main__':
    exit(main(argv))

