my_list = [i ** 3 for i in range(1, 1001, 2)]


def sum_list_1(dataset: list) -> int:
    result = 0  # объявляем счетчик конечного результата
    for my_number in dataset:
        temporary_list = [int(number) for number in str(my_number)]  # создаем временный список
        if sum(temporary_list) % 7 == 0:  # проверяем делится ли на 7 сумма цифр
            result += my_number  # если да, то добавляем к результату
    return result


def sum_list_2(dataset: list) -> int:
    result = 0
    for my_number in dataset:
        temporary_list = [int(number) for number in str(my_number+17)]  # тоже самое болько добавим 17
        if sum(temporary_list) % 7 == 0:
            result += my_number
    return result


result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
