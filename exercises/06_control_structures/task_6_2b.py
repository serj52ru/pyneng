# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите ip адрес в формате х.х.х.х: ')
ip_correct = False

while not ip_correct:
    list = ip.split('.')
    if len(list) != 4:
        print('Неправильный IP-адрес')
        ip = input('Введите ip адрес в формате х.х.х.х: ')
    elif (list[0].isdigit() and list[1].isdigit() and list[2].isdigit() and list[3].isdigit()) == ip_correct:
        print('Неправильный IP-адрес')
        ip = input('Введите ip адрес в формате х.х.х.х: ')
    elif ("." in ip) == ip_correct:
        print('Неправильный IP-адрес')
        ip = input('Введите ip адрес в формате х.х.х.х: ')
    elif (0 <= int(list[0]) <= 255 and 0 <= int(list[1]) <= 255 and 0 <= int(list[2]) <= 255 and 0 <= int(list[3]) <= 255) == ip_correct:
        print('Неправильный IP-адрес')
        ip = input('Введите ip адрес в формате х.х.х.х: ')
    else:
        ip_correct = True

if 1 <= int(list[0]) <= 223 and ip != '0.0.0.0':
    print('unicast')
elif 224 <= int(list[0]) <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')



