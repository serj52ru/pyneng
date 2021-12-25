# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

from pprint import pprint
def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_cfg = []
    key = []
    value = []

    for intf, vlan in intf_vlan_mapping.items():
        trunk_cfg.append(f'interface {intf}')
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                vlan = "".join(str(vlan)).replace("[", "").replace("]", "").replace(" ", "")
                trunk_cfg.append(f'{line} {vlan}')
            else:
                trunk_cfg.append(line)

    for line in trunk_cfg:
        if 'interface' in line:
            line = line.split()
            key.append(line[1])
        else:
            value.append(line)

    value = [value[i:i + 3] for i in range(0, len(value), 3)]

    dict_trunk_cfg = dict(zip(key, value))


    return dict_trunk_cfg


pprint(generate_trunk_config(trunk_config, trunk_mode_template))
