from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    remote_addr = line.split(' - - ')[0]
    request_type = line.split('] "')[1].split(' /')[0]
    requested_resource = line.split(' /')[1].split(' HT')[0]
    return remote_addr, request_type, requested_resource


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    while True:
        line = fr.readline()
        if not line:
            break
        list_out.append(get_parse_attrs(line))
pprint(list_out)


# Поиск спамера

def search_spam():
    spam_dict = dict()
    for ip in list_out:
        spam_dict[ip[0]] = spam_dict.get(ip[0], 0) + 1
    return max(spam_dict.items(), key=lambda x: x[1])
print(search_spam())
