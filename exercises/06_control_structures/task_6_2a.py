# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


#if "." in list:
    #if list[0].isdigit() and list[1].isdigit() and list[2].isdigit() and list[3].isdigit():






ip = input('Введите ip адрес в формате х.х.х.х: ')
list = ip.split('.')

if len(list) == 4:
    if list[0].isdigit() and list[1].isdigit() and list[2].isdigit() and list[3].isdigit():
        if "." in ip:
            if 0 <= int(list[0]) <= 255 and 0 <= int(list[1]) <= 255 and 0 <= int(list[2]) <= 255 and 0 <= int(list[3]) <= 255:
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
            else:
                print('Неправильный IP-адрес')
        else:
            print('Неправильный IP-адрес')
    else:
        print('Неправильный IP-адрес')
else:
    print('Неправильный IP-адрес')

