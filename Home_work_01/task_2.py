def check_division(digit: int) -> bool:
    """Возвращает True если сумма знаков числа кратна 7"""
    sum_numbers = 0
    while digit != 0:
        sum_numbers += digit % 10
        digit = digit // 10
    else:
        return sum_numbers % 7 == 0


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    result = 0  # объявляем счетчик конечного результата
    for digit in dataset:
        result += digit if check_division(digit) else 0
    return result


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    result = 0
    for digit in dataset:
        result += digit if check_division(digit + 17) else 0
    return result


# создаем список кубов чисел нечетных чисел
my_list = [i ** 3 for i in range(1, 1001, 2)]


result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
