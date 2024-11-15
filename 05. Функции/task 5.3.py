import csv
from prettytable import PrettyTable, ALL

field_translations = {
    "name": "Название",
    "description": "Описание",
    "key_skills": "Навыки",
    "experience_id": "Опыт работы",
    "premium": "Премиум-вакансия",
    "employer_name": "Компания",
    "salary_from": "Оклад",
    "area_name": "Название региона",
    "published_at": "Дата публикации вакансии"
}

experience_translations = {
    "noExperience": "Нет опыта",
    "between1And3": "От 1 года до 3 лет",
    "between3And6": "От 3 до 6 лет",
    "moreThan6": "Более 6 лет"
}

currency_translations = {
    "AZN": "Манаты",
    "BYR": "Белорусские рубли",
    "EUR": "Евро",
    "GEL": "Грузинский лари",
    "KGS": "Киргизский сом",
    "KZT": "Тенге",
    "RUR": "Рубли",
    "UAH": "Гривны",
    "USD": "Доллары",
    "UZS": "Узбекский сум"
}

def csv_reader(file_name):
    with open(file_name, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        titles = reader.fieldnames
        data = [v for v in reader]
    return titles, data

def formatter(row):
    row["experience_id"] = experience_translations[row["experience_id"]]
    row["salary_currency"] = currency_translations[row["salary_currency"]]

    salary_from = "{:,.0f}".format(float(row["salary_from"])).replace(",", " ")
    salary_to = "{:,.0f}".format(float(row["salary_to"])).replace(",", " ")
    salary_currency = row["salary_currency"]
    salary_gross = "Без вычета налогов" if row["salary_gross"] == "True" else "С вычетом налогов"
    row["salary_from"] = f"{salary_from} - {salary_to} ({salary_currency}) ({salary_gross})"

    del row["salary_to"], row["salary_currency"], row["salary_gross"]

    return row

def format_cell(cell):
    formatted_cell = cell.strip()
    if "\n" in formatted_cell:
        formatted_cell = ", ".join(formatted_cell.split("\n"))
    if formatted_cell == "True":
        formatted_cell = "Да"
    elif formatted_cell == "False":
        formatted_cell = "Нет"

    return formatted_cell if len(formatted_cell) <= 100 else formatted_cell[:100] + "..."

def print_vacancies(titles, vacancies):
    if not vacancies:
        print("Нет данных")
        return

    table = PrettyTable(hrules=ALL)
    table.field_names = ["№"] + [field_translations[field] for field in titles if field in field_translations]
    for field in table.field_names:
        table.align[field] = "l"
    for i, vacancy in enumerate(vacancies, start=1):
        row = [i]
        formatted_vacancy = formatter(vacancy)
        for field in titles:
            if field not in formatted_vacancy: continue
            row.append(format_cell(formatted_vacancy[field]))

        table.add_row(row)

    table.max_width = 20
    print(table)


file_name = input()
titles, vacancies = csv_reader(file_name)
print_vacancies(titles, vacancies)