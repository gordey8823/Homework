import requests
from decimal import Decimal as D
import datetime


def currency_rates(code: str) -> float:
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    code = code.upper()  # Если вдруг написали в нижнем регистре
    if response.text.count(code) == 0 or code == '':
        return None
    else:
        code = code.upper()  # Если вдруг написали в нижнем регистре
        course = response.text[response.text.index(code):response.text.index(code) + 200]
        course = course[course.index('<Value>') + 7:course.index('</Value')]
        course = course.replace(',', '.')
        course = D(course).quantize(D('1.00'))
        result_value = float(course)  # здесь должно оказаться результирующее значение float

        return result_value


def currency_rates_adv(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    code = code.upper()  # Если вдруг написали в нижнем регистре
    if response.text.count(code) == 0 or code == '':
        return None
    else:
        course = response.text[response.text.index(code):response.text.index(code) + 200]
        course = course[course.index('<Value>') + 7:course.index('</Value')]
        course = course.replace(',', '.')
        course = D(course).quantize(D('1.00'))
        result_value = float(course)  # здесь должно оказаться результирующее значение float

        # data
        date = response.text[response.text.index('Date') + 6: response.text.index('name') - 2]
        date = date.split('.')
        date = datetime.date(year=int(date[2]), month=int(date[1]), day=int(date[0]))
        return result_value, date