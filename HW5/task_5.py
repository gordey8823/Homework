def get_uniq_numbers(src: list):
    unic_numbers = set()
    second_set = set()
    for el in src:
        if el not in second_set:
            unic_numbers.add(el)
        else:
            unic_numbers.discard(el)
        second_set.add(el)
    return [el for el in src if el in unic_numbers]


src = [
    2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 8, 11, 13, 15, 15, 15,
    16, 17, 18, 18, 18, 24, 25, 27, 27, 27, 30, 30, 30, 31,
    31, 32, 32, 33, 33, 34, 35, 36, 37, 38, 39, 40, 41, 41,
    42, 43, 44, 44, 45, 45, 46, 47, 47, 48, 48, 49, 50, 50,
    51, 51, 56, 56, 57, 58, 59, 60, 60, 61, 61, 65, 66, 69,
    70, 71, 71, 71, 72, 72, 75, 75, 77, 78, 78, 79, 83, 83,
    86, 86, 89, 90, 93, 93, 94, 95, 95, 97, 98, 98, 100]
print(*get_uniq_numbers(src))






