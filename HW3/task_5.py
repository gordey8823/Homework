from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for _ in range(count)]
    return list_out


print(get_jokes(2))
print(get_jokes(10))

def get_jokes_adv(count, flag=False) -> list:
    list_out = []
    if flag == True:
        for _ in range(count):
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
                print('Шутки только эти:')
                break
            else:
                noun = choice(nouns)
                adverb = choice(adverbs)
                adjective = choice(adjectives)
                list_out.append(f'{noun} {adverb} {adjective}')
                nouns.remove(noun)
                adverbs.remove(adverb)
                adjectives.remove(adjective)
    else:
        list_out = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for _ in range(count)]

    return list_out
print(get_jokes_adv(6, True))