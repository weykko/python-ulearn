from var_dump import var_dump
import csv


class Vacancy:
    def __init__(self, name=None, description=None, key_skills=None, experience_id=None,
                 premium=None, employer_name=None, salary=None, area_name=None, published_at=None):
        self.name = name
        self.description = description
        self.key_skills = key_skills
        self.experience_id = experience_id
        self.premium = premium
        self.employer_name = employer_name
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at


class Salary:
    def __init__(self, salary_from=None, salary_to=None, salary_gross=None, salary_currency=None):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_gross = salary_gross
        self.salary_currency = salary_currency


def csv_reader(file_name):
    with open(file_name, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        titles = reader.fieldnames
        data = [v for v in reader]
    return titles, data


def load_vacancies(titles, data):
    vacancies = []
    for row in data:
        vacancy = Vacancy()
        salary = Salary()
        for field in titles:
            if field not in vacancy.__dict__ and field not in salary.__dict__: continue
            if field[:6] == "salary":
                setattr(salary, field, row[field])
            else:
                setattr(vacancy, field, row[field])

        vacancy.salary = salary
        vacancies.append(vacancy)

    return vacancies


def main():
    titles, data = csv_reader(input())
    vacancies = load_vacancies(titles, data)
    var_dump(vacancies)


if __name__ == '__main__':
    main()
