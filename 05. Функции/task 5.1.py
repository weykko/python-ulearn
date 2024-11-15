import csv

field_translations = {
    "name": "Название",
    "description": "Описание",
    "key_skills": "Навыки",
    "experience_id": "Опыт работы",
    "premium": "Премиум-вакансия",
    "employer_name": "Компания",
    "salary_from": "Нижняя граница вилки оклада",
    "salary_to": "Верхняя граница вилки оклада",
    "salary_gross": "Оклад указан до вычета налогов",
    "salary_currency": "Идентификатор валюты оклада",
    "area_name": "Название региона",
    "published_at": "Дата и время публикации вакансии"
}

def csv_reader(file_name):
    with open(file_name, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        titles = reader.fieldnames
        data = [v for v in reader]
    return titles, data

def print_vacancies(titles, vacancies):
    for i, vacancy in enumerate(vacancies):
        for field in titles:
            value = vacancy[field].strip()
            if "\n" in value:
                value = ", ".join(value.split("\n"))
            if value == "True": value = "Да"
            elif value == "False": value = "Нет"

            print(f"{field_translations[field]}: {value}")

        if i < len(vacancies) - 1: print()


file_name = input()
titles, vacancies = csv_reader(file_name)
print_vacancies(titles, vacancies)