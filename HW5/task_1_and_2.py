def odd_nums(number: int) -> int:
    """Задание №-1. Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    for i in range(1, number + 1, 2):
        yield i


def odd_nums_2(number: int):
    """Задание №-2. Аналогичен заданию №-1 за исключением ключевого слова 'yield'."""
    return (num for num in range(1, number+1, 2))

if __name__ == '__main__':
    n = 15
    generator = odd_nums(n)
    generator_2 = odd_nums_2(n)
    print('Тип генераторов:')
    print(f'Первый генератор: {type(generator)}')
    print(f'Второй генератор: {type(generator_2)}')
    print()
    print('Значения первого генератора:')
    for _ in range(1, n + 1, 2):
        print(next(generator))
    print('Значения второго генератора:')
    print(*generator_2, sep='\n')

