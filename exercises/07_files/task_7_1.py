# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

output = '{:<21}{}\n'*5

with open('ospf.txt', 'r') as f:
    for line in f:
        list_line = line.split()
        pref = list_line[1]
        metric = list_line[2].replace('[', '').replace(']', '')
        next_hop = list_line[4].replace(',', '')
        last_update = list_line[5].replace(',', '')
        intf = list_line[-1]
        print(output.format(
            'Prefix', pref,
            'AD/Metric', metric,
            'Next-Hop', next_hop,
            'Last update', last_update,
            'Outbound Interface', intf
        ))
