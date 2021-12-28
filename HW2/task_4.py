def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    # list_out = [f'Привет, {(name.split()[-1]).title()}!' for name in list_in]
    #  Или не создавая новый список
    # for index_element in range(len(list_in)):
    #    list_in[index_element] = f'Привет, {(list_in[index_element].split()[-1]).title()}!'
    # return list_out #  тут  на выбор list_in или list_out
    #  или можно сразу так
    return [f'Привет, {(name.split()[-1]).title()}!' for name in list_in]


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
