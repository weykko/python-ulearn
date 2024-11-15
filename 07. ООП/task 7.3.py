import csv
from datetime import datetime


currency_to_rub = {
    "Манаты": 35.68,
    "Белорусские рубли": 23.91,
    "Евро": 59.90,
    "Грузинский лари": 21.74,
    "Киргизский сом": 0.76,
    "Тенге": 0.13,
    "Рубли": 1,
    "Гривны": 1.64,
    "Доллары": 60.66,
    "Узбекский сум": 0.0055,
}


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


class DataSet:
    def __init__(self, file_name):
        self.titles, self.data = self._csv_reader(file_name)
        self.vacancies = self._load_vacancies(self.titles, self.data)

    @staticmethod
    def _csv_reader(file_name):
        with open(file_name, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            titles = reader.fieldnames
            data = [v for v in reader]
        return titles, data

    @staticmethod
    def _load_vacancies(titles, data):
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


class Statistics:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_salary_stat(self, profession_name):
        vacancies = self.dataset.vacancies
        # vacancies.sort(key=lambda v: datetime.strptime(v.published_at, "%H:%M:%S %d/%m/%Y").year)
        salary_year, count_year = {}, {}
        salary_year_prof, count_year_prof = {}, {}
        salary_city, count_city = {}, {}

        for vacancy in self.dataset.vacancies:
            year = datetime.strptime(vacancy.published_at, "%H:%M:%S %d/%m/%Y").year
            salary_in_rub = self._convert_salary(vacancy.salary)

            salary_year.setdefault(year, []).append(salary_in_rub)
            count_year[year] = count_year.get(year, 0) + 1

            salary_city.setdefault(vacancy.area_name, []).append(salary_in_rub)
            count_city[vacancy.area_name] = count_city.get(vacancy.area_name, 0) + 1

            if profession_name.lower() in vacancy.name.lower():
                salary_year_prof.setdefault(year, []).append(salary_in_rub)
                count_year_prof[year] = count_year_prof.get(year, 0) + 1

        avg_salary_year = {year: round(sum(salaries) / len(salaries)) for year, salaries in salary_year.items()}
        avg_salary_year_prof = {year: round(sum(salaries) / len(salaries)) for year, salaries in salary_year_prof.items()}
        avg_salary_city = {city: round(sum(salaries) / len(salaries)) for city, salaries in salary_city.items()}
        rate_salary_city = {city: round(count / len(vacancies), 4) for city, count in count_city.items()}

        sorted_avg_salary_year = dict(sorted(avg_salary_year.items(), key=lambda x: x[0]))
        sorted_count_year = dict(sorted(count_year.items(), key=lambda x: x[0]))
        sorted_avg_salary_year_prof = dict(sorted(avg_salary_year_prof.items(), key=lambda x: x[0]))
        sorted_count_year_prof = dict(sorted(count_year_prof.items(), key=lambda x: x[0]))
        sorted_avg_salary_city = dict(sorted(avg_salary_city.items(), key=lambda x: x[1], reverse=True)[:10])
        sorted_rate_salary_city = dict(sorted(rate_salary_city.items(), key=lambda x: x[1], reverse=True)[:10])

        print("Средняя зарплата по годам:", sorted_avg_salary_year)
        print("Количество вакансий по годам:", sorted_count_year)
        print(f"Средняя зарплата по годам для профессии '{profession_name}':", sorted_avg_salary_year_prof)
        print(f"Количество вакансий по годам для профессии '{profession_name}':", sorted_count_year_prof)
        print("Средняя зарплата по городам:", sorted_avg_salary_city)
        print("Доля вакансий по городам:", sorted_rate_salary_city)

    @staticmethod
    def _convert_salary(salary):
        avg_salary = (float(salary.salary_from) + float(salary.salary_to)) / 2
        return avg_salary * currency_to_rub[salary.salary_currency]


def main():
    # small_vac_50.csv
    filename = input()
    profession_name = input()
    dataset = DataSet(filename)
    statistics = Statistics(dataset)
    statistics.get_salary_stat(profession_name)


if __name__ == '__main__':
    main()