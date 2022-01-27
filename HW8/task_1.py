import re
def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'([a-zA-Z0-9\.\-\_]*)@([a-z\.\-\_]*\.(ru|com))')
    match = re.search(RE_MAIL, email)
    if match == None:
        raise ValueError('Некорректный email')
    else:
        return {'login': match.group(1), 'domen': match.group(2)}


if __name__ == '__main__':
    print(email_parse('someon_e1@geekbrains.com'))
    email_parse('someone@geekbrainsru')