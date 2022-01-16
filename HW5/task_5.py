def get_uniq_numbers(src: list):
    """Возвращает генератор уникальных чисел"""
    return (num for num in src if src.count(num) == 1)


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))