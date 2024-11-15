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

def solve():
    work = input("Введите название вакансии: ")
    description = input("Введите описание вакансии: ")
    city = input("Введите город для вакансии: ")
    experience = int(input("Введите требуемый опыт работы (лет): "))
    salary_minimum = int(input("Введите нижнюю границу оклада вакансии: "))
    salary_maximum = int(input("Введите верхнюю границу оклада вакансии: "))
    flexible_schedule = input("Нужен свободный график (да / нет): ")
    premium_vacancy = input("Является ли данная вакансия премиум-вакансией (да / нет): ")

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