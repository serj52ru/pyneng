# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий
для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно,
чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии,
но и удалять "дублирующиеся" соединения (их лучше всего видно на схеме, которую
генерирует функция draw_topology из файла draw_network_graph.py).
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Из-за того что один и тот же линк описывается дважды, на схеме будут лишние соединения.
Задача оставить только один из этих линков в итоговом словаре, не важно какой.

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии
с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть "дублирующихся" линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

import yaml
from pprint import pprint
from task_11_2a import unique_network_map
from draw_network_graph import draw_topology

def transform_topology(yaml_file):
    dict_topology = {}
    with open(yaml_file) as f:
        dict_all = yaml.safe_load(f)
        #pprint(dict_all, width=40)
        for l_dev, l_key in dict_all.items():
            #print(l_dev)
            #print(l_key)
            for l_intf, r_key in l_key.items():
                #print(l_intf)
                #print(r_key)
                for r_dev, r_intf in r_key.items():
                    #print(r_dev)
                    #print(r_intf)
                    dict_topology[(l_dev, l_intf)] = (r_dev, r_intf)
    #pprint(dict_topology)
    unique_network_map(dict_topology)
    lldp_map = unique_network_map(dict_topology)
    return lldp_map

if __name__ == "__main__":
    pprint(transform_topology("topology.yaml"))
    draw_topology(transform_topology("topology.yaml"))