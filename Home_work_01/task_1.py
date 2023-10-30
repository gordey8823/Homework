def convert_time(duration_sec: int) -> str:
    second = duration_sec % 60
    minutes = duration_sec // 60 % 60
    hours = duration_sec // 3600 % 24
    days = duration_sec // 86400

    if days:
        result = f'{days} дн {hours} час {minutes} мин {second} сек'
    elif hours:
        result = f'{hours} час {minutes} мин {second} сек'
    elif minutes:
        result = f'{minutes} мин {second} сек'
    else:
        result = f'{second} сек'
    return result


duration = 400153
result1 = convert_time(duration)
print(result1)

# для проверки циклом можно использовать рандом:
# import random
# random_seconds = [random.randint(1, 1000000) for i in range(10)]
# print(*[convert_time(duration) for duration in random_seconds], sep='\n')
