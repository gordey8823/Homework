def num_translate_adv(value: str) -> str:
    """
    Переводит числительное с английского на русский.
    Если числительное начинается с большой буквы, то и в переводе будет с большой
    """
    numbers_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }

    if value[0] == value[0].upper():
        str_out = numbers_dict.get(value.lower(), None).title()
    else:
        str_out = numbers_dict.get(value, None)

    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("Eight"))
print(num_translate_adv('nine'))
print(num_translate_adv('six'))
