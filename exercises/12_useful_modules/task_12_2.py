# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
ip_addresses = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
list_of_ips_and_ranges = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]
import ipaddress

def convert_ranges_to_ip_list(list_of_ip):
    ip_list = []
    for ip in list_of_ip:
        try:
            ipaddress.ip_network(ip)
            #print(ipaddress.IPv4Address(ip))
            ip_list.append(format(ipaddress.IPv4Address(ip)))
        except ValueError:
            network = ip.split("-")
            if network[-1].isdigit():
                new_network = network[0].split(".")
                new_network[-1] = network[-1]
                start_ip = ipaddress.IPv4Address(network[0])
                end_ip = ipaddress.IPv4Address(".".join(new_network))
                print(ipaddress.IPv4Address(".".join(new_network)))
                for ip in range(int(start_ip), int(end_ip) + 1):
                    ip_list.append(format(ipaddress.IPv4Address(ip)))
            else:
                start_ip = ipaddress.IPv4Address(network[0])
                end_ip = ipaddress.IPv4Address(network[-1])
                for ip in range(int(start_ip), int(end_ip) + 1):
                    ip_list.append(format(ipaddress.IPv4Address(ip)))


    return ip_list
if __name__ == "__main__":
    print(convert_ranges_to_ip_list(ip_addresses))
