from csv import reader
from re import sub

def read_vacancy_file(file_name):
    with open(file_name, encoding="utf_8_sig") as f:
        csv = reader(f)
        titles = next(csv)
        vacancies = [v for v in csv if len([x for x in v if x]) >= len(titles) / 2]

    return titles, vacancies

def get_dictionaries(titles, data):
    dicts = []
    for vacancy in data:
        dict = {titles[i]: clean_string(value) for i, value in enumerate(vacancy)}
        print(dict)
        dicts.append(dict)

    return dicts

def clean_string(str):
    without_html = sub("<.*?>", "", str)
    if "\n" in without_html:
        split_str = without_html.split("\n")
        cleaned_str = [" ".join(s.split()) for s in split_str]
    else:
        cleaned_str = " ".join(without_html.split())
    print(cleaned_str)
    return cleaned_str if cleaned_str else "Нет данных"

def formatted_print(output):
    for i, dict in enumerate(output):
        for key, value in dict.items():
            if isinstance(value, list): value = '; '.join(value)
            print(f"{key}: {value}")
        if i != len(output) - 1: print()

titles, vacancies = read_vacancy_file(input())
vacancies_dicts = get_dictionaries(titles, vacancies)
formatted_print(vacancies_dicts)