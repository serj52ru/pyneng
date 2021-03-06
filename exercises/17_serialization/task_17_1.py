# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""

import csv
import re
from pprint import pprint

file_list = [
             "sw1_dhcp_snooping.txt",
             "sw2_dhcp_snooping.txt",
             "sw3_dhcp_snooping.txt"
             ]

def write_dhcp_snooping_to_csv(filenames, output):

    csv_list = [["switch", "mac", "ip", "vlan", "interface"]]
    regex = r"(\S+\d+)_\S+"
    regex_2 = r"(\S+)   (\d+.\d+.\d+.\d+)\s+\d+\s+\S+\s+(\d+)\s+(\S+)"

    for file in filenames:

        hostname = re.search(regex, file)
        host = hostname.group(1)

        with open(file, "r") as f:
            for line in f:
                match = re.search(regex_2, line)
                if match:
                    csv_list.append([host, match.group(1), match.group(2), match.group(3), match.group(4)])
    print(csv_list)
    with open(output, "w") as f:
        writer = csv.writer(f)
        for row in csv_list:
            writer.writerow(row)


if __name__ == "__main__":
    write_dhcp_snooping_to_csv(file_list, "abc.csv")
    



