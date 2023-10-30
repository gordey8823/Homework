def type_logger(func):
    def wrapper(*argv, **kwargs):
        args = list(argv) + list(kwargs.values())
        result = ', '.join(f'{x}: {type(x)}' for x in args)
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(7))
"""
PyDev console: starting.
"7: <class 'int'>"
calc_cube(1, 3, 4, 7)
"1: <class 'int'>, 3: <class 'int'>, 4: <class 'int'>, 7: <class 'int'>"
calc_cube(1, 3, 4.2, ['7'])
"1: <class 'int'>, 3: <class 'int'>, 4.2: <class 'float'>, ['7']: <class 'list'>"
calc_cube(1, 3, 4.2, ['7'], a=2)
"1: <class 'int'>, 3: <class 'int'>, 4.2: <class 'float'>, ['7']: <class 'list'>, 2: <class 'int'>"
"""