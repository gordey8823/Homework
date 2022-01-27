import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    line = fr.readline()
    # Первый вариант но попадают адреса вида 2001:4801:7824:102:8bee:6e66:ff10:6aa2
    #PARSE_LINE = re.compile(r'(\S+)[\s-]*\[(.*)\]\s"(\w*)\s(/\w*/\w*)\s\w+/\d\.\d.\s(\d+)\s(\d+)')
    # Второй вариант но попадаем на AttributeError

    PARSE_LINE = re.compile(r'(\d+\.\d+\.\d+\.\d+)[\s-]*\[(.*)\]\s"(\w*)\s(/\w*/\w*)\s\w+/\d\.\d.\s(\d+)\s(\d+)')
    while line:
        match = re.search(PARSE_LINE, line)
        try:
            print((match.group(1), match.group(2), match.group(3), match.group(4), match.group(5), match.group(6)))
        except AttributeError as err:
            print(f'ip некорректен {line}')
        line = fr.readline()
