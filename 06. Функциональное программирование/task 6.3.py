from datetime import datetime
from prettytable import PrettyTable, ALL
import csv
import re

def csv_reader(file_name):
    with open(file_name, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        titles = reader.fieldnames
        data = [v for v in reader]
    return titles, data

def format_cell(cell):
    formatted_cell = cell.strip()
    if "\n" in formatted_cell:
        formatted_cell = ", ".join(formatted_cell.split("\n"))
    return formatted_cell if len(formatted_cell) <= 100 else formatted_cell[:100] + "..."

def get_range(rows, columns):
    range = {}
    if rows:
        nums = [int(n) for n in rows.split()]
        range["start"] = nums[0] - 1
        if len(nums) > 1: range["end"] = nums[1]

    if columns:
        strings = columns.split(", ")
        strings.append("№")
        range["fields"] = strings

    return range

def filter_data(data, filter_parameters):
    filter, value = filter_parameters.split(": ")
    filtered_data = []
    for vacancy in data:
        if filter == "Оклад":
            salary = [int(n.replace(" ", "")) for n in re.findall(r"\d{1,3}(?:\s\d{3})*", vacancy["Оклад"])]
            if salary[0] <= int(value) <= salary[1]: filtered_data.append(vacancy)
        elif filter == "Идентификатор валюты оклада":
            if value in vacancy["Оклад"]: filtered_data.append(vacancy)
        else:
            if value in vacancy[filter]: filtered_data.append(vacancy)

    return  filtered_data

def sort_data(data, field, is_reverse):
    if field == "Оклад":
        data.sort(key=lambda v: int(re.findall(r"\d{1,3}(?:\s\d{3})*", v["Оклад"])[1].replace(" ", "")), reverse=is_reverse)
    elif field == "Опыт работы":
        data.sort(key=lambda v: (
            numbers := re.findall(r"\d+", v["Опыт работы"]),
            int(numbers[0]) if numbers else 0
        ), reverse=is_reverse)
    elif field == "Дата публикации вакансии":
        data.sort(key=lambda v: datetime.strptime(v["Дата публикации вакансии"], "%H:%M:%S %d/%m/%Y"), reverse=is_reverse)
    return data

def get_table(titles, vacancies):
    if not vacancies:
        print("Нет данных")
        return

    table = PrettyTable(hrules=ALL)
    table.field_names = ["№"] + titles
    for field in table.field_names: table.align[field] = "l"
    for i, vacancy in enumerate(vacancies, start=1):
        row = [i]
        for field in titles:
            row.append(format_cell(vacancy[field]))

        table.add_row(row)

    table.max_width = 20

    return table

file_name = input()
filter_parameters = input()
sort_field = input()
is_reverse = True if input() == "Да" else False
range = get_range(input(), input())

titles, vacancies = csv_reader(file_name)

if filter_parameters: vacancies = filter_data(vacancies, filter_parameters)
if sort_field: vacancies = sort_data(vacancies, sort_field, is_reverse)

table = get_table(titles, vacancies)
# vacancies_for_functional.csv
print(table.get_string(**range))
