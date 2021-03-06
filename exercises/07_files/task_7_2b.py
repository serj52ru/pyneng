# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
file = argv[1]
to_file = argv[2]
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

cfg_str = ''.join(list)

with open(to_file, 'w') as f:
    f.write(cfg_str)

print(cfg_str)