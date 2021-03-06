# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

list_of_ip = ["8.8.8.8", "172.16.1.254", "10.0.0.1"]

def ping_ip_addresses(ip_list):
    reacheble_ip = []
    unreacheble_ip = []

    for ip in ip_list:
        ping = subprocess.run(["ping", "-c", "2", ip], stdout=subprocess.PIPE)
        if ping.returncode:
            unreacheble_ip.append(ip)
        else:
            reacheble_ip.append(ip)
    tuple_of_ip = (reacheble_ip, unreacheble_ip)

    return tuple_of_ip

if __name__ == "__main__":
    print(ping_ip_addresses(list_of_ip))