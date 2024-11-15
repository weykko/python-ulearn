def years_declination(value):
    last_digit = value % 10
    last_two_digits = value % 100
    if last_digit == 1 and last_two_digits != 11: return "год"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14): return "года"
    return "лет"

def rubles_declination(value):
    last_digit = value % 10
    last_two_digits = value % 100
    if last_digit == 1 and last_two_digits != 11: return "рубль"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14): return "рубля"
    return "рублей"

def string_input(text):
    while True:
        s = input(text).strip()
        if s: return s
        print("Данные некорректны, повторите ввод")

def int_input(text):
    while True:
        s = input(text)
        if s.isdigit(): return int(s)
        print("Данные некорректны, повторите ввод")

def bool_input(text):
    while True:
        s = input(text)
        if s in ["да", "нет"]: return s
        print("Данные некорректны, повторите ввод")

def solve():
    work = string_input("Введите название вакансии: ")
    description = string_input("Введите описание вакансии: ")
    city = string_input("Введите город для вакансии: ")
    experience = int_input("Введите требуемый опыт работы (лет): ")
    salary_minimum = int_input("Введите нижнюю границу оклада вакансии: ")
    salary_maximum = int_input("Введите верхнюю границу оклада вакансии: ")
    flexible_schedule = bool_input("Нужен свободный график (да / нет): ")
    premium_vacancy = bool_input("Является ли данная вакансия премиум-вакансией (да / нет): ")

    average_salary = int((salary_minimum + salary_maximum) / 2)

    print(
f"""{work}
Описание: {description}
Город: {city}
Требуемый опыт работы: {experience} {years_declination(experience)}
Средний оклад: {average_salary} {rubles_declination(average_salary)}
Свободный график: {flexible_schedule}
Премиум-вакансия: {premium_vacancy}""")

solve()