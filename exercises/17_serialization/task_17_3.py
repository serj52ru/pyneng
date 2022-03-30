# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

from pprint import pprint
import re

def parse_sh_cdp_neighbors(show_str):

    regex_hostname = r"(\S+)>"
    regex_cdp = r"(?P<dev_id>\S+)\s+(?P<local_intf>\S+ \S+)\s+\S+\s+R S I\s+\S+\s+(?P<port_id>\S+ \S+)"
    cdp_dict = {}
    local = {}
    for line in show_str.split("\n"):
        print(line)
        if line:
            match_hostname = re.search(regex_hostname, line)
            match_cdp = re.search(regex_cdp, line)

            if match_hostname:
                hostname = match_hostname.group(1)
                print(hostname)
            elif match_cdp:
                port_id = match_cdp.group("port_id")
                local_intf = match_cdp.group("local_intf")
                dev_id = match_cdp.group("dev_id")
                local[local_intf] = {dev_id: port_id}

    cdp_dict[hostname] = local
    #pprint(cdp_dict)
    return cdp_dict


if __name__ == "__main__":
    f = open("sh_cdp_n_sw1.txt", "r")
    print(parse_sh_cdp_neighbors(f.read()))