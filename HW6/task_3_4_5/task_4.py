import json
import sys

with open('task_6_3_result.json', 'r', encoding='utf-8') as fr:
    dict_users_hobby = json.load(fr)

    with open('users_hobby.txt', 'w', encoding='utf-8') as fw:
        list_hobby_users = []
        for key, value in dict_users_hobby.items():
            list_hobby_users.append(f'{key}: {value}')
            list_hobby_users.append('\n')
        fw.writelines(list_hobby_users)
