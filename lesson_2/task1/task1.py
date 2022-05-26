import re
import csv


def get_data():
    re_producer = re.compile(r'^Изготовитель системы:\s*(.*)$')
    re_os = re.compile(r'^Изготовитель ОС:\s*(.*)$')
    re_code = re.compile(r'^Код продукта:\s*(.*)$')
    re_system = re.compile(r'^Тип системы:\s*(.*)$')

    expressions = [re_producer, re_os, re_code, re_system]

    results = [[], [], [], []]
    main_data = [["Изготовитель системы", "Изготовитель ОС", "Код продукта", "Тип системы"]]

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as f:
            for line in f.readlines():
                line = line.decode("windows-1251").strip()

                for j in range(4):
                    match = expressions[j].search(line)
                    if match:
                        results[j].append(match.group(1))

    result_length = len(results[0])
    for j in range(result_length):
        temp_list = []
        for i in range(4):
            temp_list.append(results[i][j])
        main_data.append(temp_list)

    return main_data


def write_to_csv(filepath):
    with open(filepath, 'w') as f:
        csv.writer(f).writerows(get_data())


write_to_csv('test.csv')
