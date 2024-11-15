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
        dicts.append(dict)

    return dicts

def clean_string(str):
    without_html = sub("<.*?>", "", str)
    if "\n" in without_html:
        split_str = without_html.split("\n")
        cleaned_str = [" ".join(s.split()) for s in split_str]
    else:
        cleaned_str = " ".join(without_html.split())

    return cleaned_str if cleaned_str else "Нет данных"

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):flat_list.extend(flatten(item))
        else: flat_list.append(item)
    return flat_list

def times_declination(value):
    last_digit = value % 10
    last_two_digits = value % 100
    if 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return "раза"
    return "раз"

def rubles_declination(value):
    last_digit = value % 10
    last_two_digits = value % 100
    if last_digit == 1 and last_two_digits != 11:
        return "рубль"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return "рубля"
    return "рублей"

def vacancy_declination(value):
    last_digit = value % 10
    last_two_digits = value % 100
    if last_digit == 1 and last_two_digits != 11:
        return "вакансия"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return "вакансии"
    return "вакансий"

def get_analysis(vacancies_dicts):
    correct_vacancies = [vacancy for vacancy in vacancies_dicts if vacancy["salary_currency"] == "RUR"]
    salaries_data = []
    for vacancy in correct_vacancies:
        if vacancy["salary_to"] == "Нет данных":
            avg = int(float(vacancy["salary_from"]) // 2)
        elif vacancy["salary_from"] == "Нет данных":
            avg = int(float(vacancy["salary_to"]) // 2)
        else:
            avg = int((float(vacancy["salary_from"]) + float(vacancy["salary_to"])) // 2)
        salaries_data.append((vacancy["name"], vacancy["employer_name"], avg, vacancy["area_name"]))

    skills = flatten([row["key_skills"] for row in correct_vacancies])
    skills_data = {}
    for skill in skills:
        if skill in skills_data:
            skills_data[skill] += 1
        else:
            skills_data[skill] = 1

    cities = [row["area_name"] for row in correct_vacancies]
    cities_data = {}
    for city in cities:
        if city in cities_data: continue
        city_salaries = [salary for salary in salaries_data if salary[3] == city]
        salaries_count = len(city_salaries)
        if salaries_count < len(salaries_data) // 100: continue
        cities_data[city] = (sum(salary[2] for salary in city_salaries) // salaries_count, salaries_count)

    highest_salaries = sorted(salaries_data, key=lambda x: x[2], reverse=True)[:10]
    lowest_salaries = sorted(salaries_data, key=lambda x: x[2])[:10]
    popular_skills = sorted(skills_data.items(), key=lambda x: x[1], reverse=True)[:10]
    highest_city_salaries = sorted(cities_data.items(), key=lambda x: x[1][0], reverse=True)[:10]

    print("Самые высокие зарплаты:")
    for i, (name, employer, salary, city) in enumerate(highest_salaries):
        print(f"    {i + 1}) {name} в компании \"{employer}\" - {salary} {rubles_declination(salary)} (г. {city})")
    print()

    print("Самые низкие зарплаты:")
    for i, (name, employer, salary, city) in enumerate(lowest_salaries):
        print(f"    {i + 1}) {name} в компании \"{employer}\" - {salary} {rubles_declination(salary)} (г. {city})")
    print()

    print(f"Из {len(set(skills))} скиллов, самыми популярными являются:")
    for i, (skill, count) in enumerate(popular_skills):
        print(f"    {i + 1}) {skill} - упоминается {count} {times_declination(count)}")
    print()

    print(f"Из {len(set(cities))} городов, самые высокие средние ЗП:")
    for i, (city, (avg_salary, count)) in enumerate(highest_city_salaries):
        print(f"    {i + 1}) {city} - средняя зарплата {avg_salary} {rubles_declination(avg_salary)} ({count} {vacancy_declination(count)})")

titles, vacancies = read_vacancy_file(input())
vacancies_dicts = get_dictionaries(titles, vacancies)
get_analysis(vacancies_dicts)