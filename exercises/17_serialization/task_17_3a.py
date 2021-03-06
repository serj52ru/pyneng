# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import glob
from pprint import pprint
import re
import yaml


sh_cdp_n = glob.glob("sh_cdp_n_*")
#pprint(sh_cdp_n)
def generate_topology_from_cdp(list_of_files, save_to_filename=None):

    regex_hostname = r"(\S+)>"
    regex_cdp = r"(?P<dev_id>\S+)\s+(?P<local_intf>Eth \S+)\s+\S+\s+R? S I\s+\S+ ?\S+?\s+(?P<port_id>Eth \S+)"
    cdp_dict = {}
    for file in list_of_files:
        #print(file)
        f = open(file, "r")
        file_str = f.read()

        local = {}
        for line in file_str.split("\n"):
            #print(line)
            if line:
                #pprint(line)
                match_hostname = re.search(regex_hostname, line)
                match_cdp = re.search(regex_cdp, line)

                if match_hostname:
                    hostname = match_hostname.group(1)
                    #print(hostname)
                elif match_cdp:
                    #print(match_cdp.group())
                    port_id, local_intf, dev_id = match_cdp.group("port_id", "local_intf", "dev_id")
                    local[local_intf] = {dev_id: port_id}
        cdp_dict[hostname] = local
    #pprint(cdp_dict)

    if save_to_filename:
        #print(save_to_filename)
        with open(save_to_filename, "w") as f:
            cfg = yaml.dump(cdp_dict, f)

    return cdp_dict


if __name__ == "__main__":
    pprint(generate_topology_from_cdp(sh_cdp_n, "topology.yaml"))