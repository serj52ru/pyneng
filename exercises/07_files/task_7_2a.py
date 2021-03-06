# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
file = argv[1]

list = []

with open(file, 'r') as f:
    for line in f:
        if not line.startswith('!'):
            if not ('alias' in line):
                list.append(line)

for i in list:
    if 'duplex' in i:
        list.remove(i)
    elif ignore[2] in i:
        list.remove(i)

print(''.join(list))

