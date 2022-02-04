from abc import ABC


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def calculate(self):
        return float(f'{self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}')


class Coat(Clothes):
    def calculate(self):
        return float(f'{self.param / 6.5 + 0.5 :.2f}')


class Costume(Clothes):
    def calculate(self):
        return float(f'{2 * self.param + 0.3 :.2f}')


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate())  # 7.42
    print(costume.calculate())  # 6.3
