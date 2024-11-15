from csv import reader

def read_vacancy_file(file_name):
    with open(file_name, encoding="utf_8_sig") as f:
        csv = reader(f)
        titles = next(csv)
        vacancies = [v for v in csv if len([x for x in v if x]) >= len(titles) / 2]

    return titles, vacancies

titles, vacancies = read_vacancy_file(input())
print(titles)
print(vacancies)
