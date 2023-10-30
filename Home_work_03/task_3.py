def thesaurus(*args) -> dict:
    """
    Принимает на вход имена через запятую в виде- "Иван"
    Возвращает словарь где первая буква имени - это ключ, а значением по этому
    ключу будет список из имен начинающихся на эту букву
    """
    # пишите свою реализацию здесь
    names = {name.title() for name in args}
    first_letter = [name[0].upper() for name in names]
    dict_out = {k: list() for k in first_letter}
    for name in names:
        dict_out[name[0]].append(name)
    return dict_out


print((thesaurus("Иван", "Мария", "Петр", "Илья", "Илья")))
