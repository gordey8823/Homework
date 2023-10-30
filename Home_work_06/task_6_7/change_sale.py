import sys


def change_sale(argv):
    # Проверка. Существует ли запись. Если да то записываем построчно в bakery_copy.csv
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        line = fr.readline()
        count = 0
        while line:
            count += 1
            line = fr.readline()
    if int(argv[1]) > count > 0:
        print('Несуществующая запись, попробуйте ввести другую запись')
    else:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            line = fr.readline()
            count = 1
            while line:
                if count == int(argv[1]):
                    with open('bakery_copy.csv', 'a', encoding='utf-8') as af:
                        af.write(argv[2].ljust(10) + '\n')
                        line = fr.readline()
                else:
                    with open('bakery_copy.csv', 'a', encoding='utf-8') as af:
                        af.write(line)
                        line = fr.readline()
                count += 1

        # стираем данные из bakery.csv
        with open('bakery.csv', 'w', encoding='utf-8') as fw:
            fw.write('')

        # и записываем в него из созданной нами копии
        with open('bakery_copy.csv', 'r', encoding='utf-8') as fr:
            line = fr.readline()
            while line:
                with open('bakery.csv', 'a', encoding='utf-8') as fa:
                    fa.write(line)
                line = fr.readline()

        with open('bakery_copy.csv', 'w', encoding='utf-8') as fw:
            fw.write('')
    # Сильно не бейте, сделал как мог :)


if __name__ == '__main__':
    exit(change_sale(sys.argv))
