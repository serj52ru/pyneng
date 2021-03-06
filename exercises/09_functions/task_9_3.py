# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from pprint import pprint

def get_int_vlan_map(config_filename):
    with open(config_filename) as file:
        intf = []
        for line in file:
            if "Fast" in line:
                line = line.split()
                intf.append(line[1])
            elif "access vlan" in line:
                line = line.split()[-1]
                intf.append(int(line))
            elif "trunk allowed vlan" in line:
                line = line.split()[-1].split(",")
                result = [int(item) for item in line]
                intf.append(result)

    intf = [intf[i:i + 2] for i in range(0, len(intf), 2)]

    for i in intf:
        if len(i) != 2:
            intf.pop(-1)

    access_dict = {}
    trunk_dict = {}
    tuple_cfg = (access_dict, trunk_dict)

    for interface, vlan in intf:
        if type(vlan) == list:
            trunk_dict[interface] = vlan
        else:
            access_dict[interface] = vlan

    return tuple_cfg

pprint(get_int_vlan_map("config_sw1.txt"))

