def try_to_bool(value):
    return value == "да" if value in ["да", "нет"] else value

def try_to_int(value):
    return int(value) if value.isdigit() else value

def formatted_print(value):
    print(f"{value} ({type(value).__name__})")

def solve():
    work = input("Введите название вакансии: ")
    description = input("Введите описание вакансии: ")
    city = input("Введите город для вакансии: ")
    experience = input("Введите требуемый опыт работы (лет): ")
    salary_minimum = input("Введите нижнюю границу оклада вакансии: ")
    salary_maximum = input("Введите верхнюю границу оклада вакансии: ")
    flexible_schedule = input("Нужен свободный график (да / нет): ")
    premium_vacancy = input("Является ли данная вакансия премиум-вакансией (да / нет): ")

    formatted_print(work)
    formatted_print(description)
    formatted_print(city)
    formatted_print(try_to_int(experience))
    formatted_print(try_to_int(salary_minimum))
    formatted_print(try_to_int(salary_maximum))
    formatted_print(try_to_bool(flexible_schedule))
    formatted_print(try_to_bool(premium_vacancy))

solve()