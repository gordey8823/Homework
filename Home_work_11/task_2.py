class DivisionByNull:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide_by_null(dividend, divider):
        try:
            return dividend / divider
        except:
            return "Деление на ноль недопустимо"


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
