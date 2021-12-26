my_list = [i ** 3 for i in range(1, 1001, 2)]


def sum_list_1(dataset: list) -> int:
    result = 0  # объявляем счетчик конечного результата
    for my_number in dataset:
        # n1 = my_number % 10
        # n2 = my_number // 10 % 10
        # n3 = my_number // 100 % 10
        # n4 = my_number // 1000 % 10
        # n5 = my_number // 10000 % 10
        # n6 = my_number // 100000 % 10
        # n7 = my_number // 1000000 % 10
        # n8 = my_number // 10000000 % 10
        # n9 = my_number // 100000000 % 10
        # n10 = my_number // 1000000000 % 10
        # n11 = my_number // 10000000000 % 10
        # if (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11) % 7 == 0:
        #     result += my_number
        summ_my_namber = 0
        my_number_copy = my_number
        while my_number != 0:
            summ_my_namber += (my_number % 10)
            my_number = my_number // 10
        else:
            if summ_my_namber % 7 == 0:
                result += my_number_copy
            summ_my_namber = 0

    return result


def sum_list_2(dataset: list) -> int:
    result = 0
    for my_number in dataset:
        # n1 = (my_number + 17) % 10
        # n2 = (my_number + 17) // 10 % 10
        # n3 = (my_number + 17) // 100 % 10
        # n4 = (my_number + 17) // 1000 % 10
        # n5 = (my_number + 17) // 10000 % 10
        # n6 = (my_number + 17) // 100000 % 10
        # n7 = (my_number + 17) // 1000000 % 10
        # n8 = (my_number + 17) // 10000000 % 10
        # n9 = (my_number + 17) // 100000000 % 10
        # n10 = (my_number + 17) // 1000000000 % 10
        # n11 = (my_number + 17) // 10000000000 % 10
        # if (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11) % 7 == 0:
        #     result += my_number +17
        summ_my_namber = 0
        my_number_copy = my_number +17
        while my_number_copy != 0:
            summ_my_namber += (my_number_copy % 10)
            my_number_copy = my_number_copy // 10
        else:
            if summ_my_namber % 7 == 0:
                result += my_number + 17
            summ_my_namber = 0
    return result


result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
