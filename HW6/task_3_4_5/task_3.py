import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as ru:
        line = ru.readline()
        full_names = []
        while line:
            line = line.strip()
            full_names.append(line.replace(',', ' '))
            line = ru.readline()

    with open(path_hobby_file, 'r', encoding='utf-8') as rh:
        line = rh.readline()
        full_hobbies = []
        while line:
            line = line.strip()
            full_hobbies.append(line.replace(',', ', '))
            line = rh.readline()

    if len(full_names) < len(full_hobbies):
        return 1
    else:
        hobby_users = [(user, full_hobbies[index]) if len(full_hobbies) > index else (user, None)
                       for index, user in enumerate(full_names)]
        hobby_users_dict = {el[0]: el[1] for el in hobby_users}
        return hobby_users_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
