def transform_string(number: int) -> str:
    if number % 10 == 1 and number % 100 != 11:
        result = f'{number} процент'
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 > 20):
        result = f'{number} процента'
    else:
        result = f'{number} процентов'
    return result


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
