import sys
from utils import currency_rates

def main(ardv):
    if not ardv:
        return 'Введите код валюты'
    else:
        print(currency_rates(ardv[1]))

if __name__ == '__main__':
    exit(main(sys.argv))

# PS C:\Users\ убрал знак \ , из за него ругалась программа

"""
PS C:Users\pavel\Desktop\PythonB\leason_4> python task_4.py USD
74.57
PS C:Users\pavel\Desktop\PythonB\leason_4> python task_4.py gbp
102.49
PS C:Users\pavel\Desktop\PythonB\leason_4> python task_4.py AMd
15.45
PS C:Users\pavel\Desktop\PythonB\leason_4> python task_4.py Brl
13.47
"""