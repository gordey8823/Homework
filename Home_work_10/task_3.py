class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        return self.__class__(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return self.__class__(self.cells - other.cells)
        raise ValueError(f'недопустимая операция')

    def __mul__(self, other):
        return self.__class__(self.cells * other.cells)

    def __floordiv__(self, other):
        return self.__class__(self.cells // other.cells)

    def __truediv__(self, other):
        return self.__class__(self.cells / other.cells)

    def make_order(self, cols):
        result = []
        for row in range(self.cells // cols):
            result_row = []
            for _ in range(cols):
                result_row.append('*')
            result.append(''.join(result_row))
        result_row = []
        for el in range(self.cells % cols):
            result_row.append('*')
        result.append(''.join(result_row))
        result = '\n'.join(result)
        print(result)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция
    try:
        print(type(cell_1))
        cell_1 * 123

    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса

