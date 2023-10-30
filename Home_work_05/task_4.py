from random import randint
def get_numbers(src: list):
    """Возвращает генератор чисел из списка если число больше предыдущего."""
    return (src[index] for index in range(1, len(src)) if src[index] > src[index - 1])



src = [randint(0, 100) for i in range(20)]
print(*src)
print(*get_numbers(src))