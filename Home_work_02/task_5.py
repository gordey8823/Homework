from random import uniform
from copy import deepcopy


# Задание a)___________________________________________________________________________________________________
def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    for price in list_in:
        rubles = int(price)
        kopecks = price * 100 % 100
        list_in[list_in.index(price)] = f'{int(rubles):02} руб. {int(kopecks):02} коп.'

    str_out = ''
    for price in list_in:
        str_out += price
        if list_in.index(price) == len(list_in) - 1:
            break
        str_out += ', '

    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
my_list_copy = deepcopy(my_list)  # пришлось создать копию так как влияло на другие решения
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list_copy)
print(result_1)


# Задание b)__________________________________________________________________________________________________

# def sort_prices(list_in: list) -> None:
#     """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
#     return list_in.sort()
"""Если использовать функцию то метод sotr возвращает None, но и то объект будет другой,
но если использовать sorted то возвращает отсортированный список и все равно объект уже другой.
Поэтому только так:     """
print(id(my_list))
my_list.sort()
print(id(my_list))
print(my_list)


# Задание с)____________________________________________________________________________________________________
def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""

    list_out = sorted(list_in, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


# Задание d)__________________________________________________________________________________________________
def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_in.sort(reverse=True)
    list_out = list_in[:5]
    list_out.sort()
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
