# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
from pprint import pprint
import csv

sh_version_files = glob.glob("sh_vers*")
sh_version_files = sorted(sh_version_files)
print(sh_version_files)

headers = ["hostname", "ios", "image", "uptime"]




def parse_sh_version(file_str):

    file = file_str.split("\n")
    regex_ios = r"Cisco IOS .+ Version (?P<ios>\d\d.\d[(]\d+[)]\S+),"
    regex_image = r'System image file is (?P<image>\S+:\S+)'
    regex_uptime = r"router uptime is (?P<uptime>\d+ days, \d+ hours, \d+ minutes)"
    list_info = []
    for line in file:
        #print(line)
        ios = re.search(regex_ios, line)
        image = re.search(regex_image, line)
        uptime = re.search(regex_uptime, line)

        if ios:
            ios = ios.group("ios")
            list_info.append(ios)
            #print(ios)
        elif image:
            image = image.group("image")
            list_info.append(image.replace('"', ''))
        elif uptime:
            uptime = uptime.group("uptime")
            list_info.append(uptime.replace('"', ''))
            #print(uptime)

    sh_ver_tuple = tuple(list_info)
    #print(sh_ver_tuple)
    return sh_ver_tuple


def write_inventory_to_csv(data_filenames, csv_filename):
    data = []
    data.append(headers)

    for file in data_filenames:
        list_file = []
        regex_hostname = r"\S+_(\S+).txt"
        match = re.search(regex_hostname, file)
        hostname = match.group(1)
        print(hostname)

        with open(file, "r") as f:
            file_str = f.read()
            tuple_info = parse_sh_version(file_str)
            list_file.append(hostname)
            list_file.append(tuple_info[0])
            list_file.append(tuple_info[2])
            list_file.append(tuple_info[1])

        with open(csv_filename, "w") as f:
            #data.append(headers)
            data.append(list_file)
            print(data)
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)



if __name__ == "__main__":
    write_inventory_to_csv(sh_version_files, "routers_inventory.csv")
