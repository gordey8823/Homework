def thesaurus_adv(*args):
    """
    Принимает на вход имя и фамилию через запятую в виде- "Иван Иванов"
    Возвращает словарь где первая буква фамилии - это ключ, а значением по этому
    ключу будет словарь из первых букв имени значениями которых будет спислок из имени и фамилии
    """
    out_dict = {}
    for elem in args:
        name, second_name = elem.split()
        if not out_dict.get(second_name[0]):
            out_dict[second_name[0]] = {name[0]: [elem]}
        elif not out_dict[second_name[0]].get(name[0]):
            (out_dict[second_name[0]])[name[0]] = [elem]
        else:
            (out_dict[second_name[0]])[name[0]].append(elem)

    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
