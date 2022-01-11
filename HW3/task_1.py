def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
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

    str_out = numbers_dict.get(value, None)
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate('nhb'))
