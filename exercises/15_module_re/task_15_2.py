# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""

import re
from pprint import pprint

def parse_sh_ip_int_br(file):

    regex = r"(\S+\d)\s+(\S+)\s+\S+\s+\S+\s+((administratively down)|(up)|(down))\s+((up)|(down))"
    cfg_list = []
    with open(file, "r") as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                #print(match.group(7))
                intf_tuple = (match.group(1), match.group(2), match.group(3), match.group(7))
                cfg_list.append(tuple(intf_tuple))
        #print(cfg_list)

    return cfg_list

if __name__ == "__main__":
    pprint(parse_sh_ip_int_br("sh_ip_int_br.txt"))
