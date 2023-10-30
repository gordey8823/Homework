tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = [
    '9А', '7В', '9Б', '9В', '8Б' #, '10А', '10Б', '9А'
]


def check_gen(tutors: list, klasses: list):
    """
    Генерато возвращающий список из кортежей в виде ('Иван', '9А'),
    если список klasses больше tutors, возвращает ('Елена','None')
    """
    return ((tutor, klasses[index]) if index < len(klasses) else (tutor, None) for index, tutor in enumerate(tutors))


generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
