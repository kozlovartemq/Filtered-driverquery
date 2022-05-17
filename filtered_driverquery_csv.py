import subprocess
import csv
from typing import List


def run_driverquery_as_csv() -> List[list]:
    command = f'driverquery /fo csv'
    output = subprocess.check_output(command).decode('cp866')
    list_of_output = output.split('\n')
    result = [item.split(',') for item in list_of_output]

    for i in range(len(result)):  # Удаление управляющего символа '\r' в последних айтемах
        new_last_item = result[i][-1].replace('\r', '')
        result[i].pop(-1)
        result[i].append(new_last_item)
    print('A data has been collected.')
    return result


def save_csv_file(csv_data: List[list]):
    with open('drivers.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in csv_data:
            writer.writerow(row)
    print('A CSV file was created.')


def print_selected_rows_of_csv():
    with open('drivers.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        d_reader = csv.DictReader(csvfile)
        headers = d_reader.fieldnames  # Получение названий колонок
        d_headers = {}
        for index, header in enumerate(headers):  # Получение индексов для названий колонок
            d_headers[header] = index
        print('Названия колонок в файле:', *headers)
        column = ''
        while column not in headers:
            column = input('Введите название колонки, по которому будет выполнятся фильтрация: ')
            if column not in headers:
                print('Нет такого названия.')
        value = input('Введите нужное значение: ')
        for row in reader:
            if len(row) == len(headers) and value in row[d_headers[column]]:  # Для предотвращения исключения Out of range
                selected_row = ', '.join(row)
                print(selected_row)


def main():
    data = run_driverquery_as_csv()
    save_csv_file(csv_data=data)
    print_selected_rows_of_csv()


if __name__ == '__main__':
    main()
