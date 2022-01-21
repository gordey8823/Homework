from russian_names import RussianNames
"""
!!!ВНИМАНИЕ!!!
Для скрипта требуется библиотека "russian_names"
"""

count_users = 30  # Введите количество персон
users = list(RussianNames(count=count_users).get_batch())
users_adv = []
for user in users:
    user_new = user.split()
    users_adv.append(','.join(user_new))
    users_adv.append('\n')
users_adv.pop(-1)


with open('users.csv', 'w', encoding='utf-8') as f:
    for user in users_adv:
        f.writelines(user)

