# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a
на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них.

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким
образом, чтобы в значении словаря она возвращала список кортежей
для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет
несколько кортежей. Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность
IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""

import re
from pprint import pprint

def get_ip_from_cfg(file):

    regex = r"^interface (\S+)"
    regex_ip = r" ip address (\d+.\d.+\d.+\d+) (\d+.\d.+\d.+\d+)"
    dict_ip = {}
    with open(file, "r") as f:
        for line in f:
            match = re.search(regex, line)
            match_ip = re.search(regex_ip, line)
            if match:
                key = match.group(1)
                list_ip = []
            elif match_ip:
                value = (match_ip.group(1), match_ip.group(2))
                list_ip.append(value)
                dict_ip[key] = list_ip

    return dict_ip
if __name__ == "__main__":
    print(get_ip_from_cfg("config_r2.txt"))