def convert_time(duration: int) -> str:
    second = duration % 60
    minutes = duration // 60 % 60
    hourse = duration // 3600 % 24
    days = duration // 86400

    if days > 0:
        result = f'{days} дн {hourse} час {minutes} мин {second} сек'
    elif hourse > 0:
        result = f'{hourse} час {minutes} мин {second} сек'
    elif minutes > 0:
        result = f'{minutes} мин {second} сек'
    else:
        result = f'{second} сек'
    return result



duration = 153
result1 = convert_time(duration)
print(result1)

# для проверки циклом можно использовать рандом:
# import random
# random_seconds = [random.randint(1, 1000000) for i in range(10)]
# print(*[convert_time(duration) for duration in random_seconds], sep='\n')