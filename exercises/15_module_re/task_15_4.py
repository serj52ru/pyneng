# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""

import re
from pprint import pprint

def get_ints_without_description(file):

    intf_list_all = []
    intf_list = []
    intf_list_end = []

    regex_intf = r"^interface (\S+)"

    with open(file, "r") as f:
        for line in f:
            match_intf = re.search(regex_intf, line)
            if match_intf:
                intf = match_intf.group(1)
                intf_list_all.append(intf)
            elif " description " in line:
                intf_list.append(intf)

        for intf in intf_list_all:
            if intf not in intf_list:
                intf_list_end.append(intf)

    return intf_list_end

if __name__ == "__main__":
    print(get_ints_without_description("config_r1.txt"))
