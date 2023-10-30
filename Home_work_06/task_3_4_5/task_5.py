from task_3 import prepare_dataset
import sys


def main(argv):
    program, argv1, argv2, argv3 = argv
    dict_users_hobby = prepare_dataset(argv1, argv2)
    with open(argv3, 'w', encoding='utf-8') as fw:
        list_hobby_users = []
        for key, value in dict_users_hobby.items():
            list_hobby_users.append(f'{key}: {value}')
            list_hobby_users.append('\n')
        fw.writelines(list_hobby_users)


if __name__ == '__main__':
    exit(main(sys.argv))
