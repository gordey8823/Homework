class OfficeEquipment:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


p = Printer('Hp', 2, 300)
s = Scanner('Canon', 54000, 10)
x = Xerox('Xerox', 7000, 15)
p.income()
s.income()
x.income()
