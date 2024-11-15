from prettytable import PrettyTable, ALL
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


class Utils:
    @classmethod
    def create_table(cls, dataset):
        titles, vacancies = dataset.titles, dataset.vacancies
        table = PrettyTable(hrules=ALL, align="l")
        table.field_names = ["№"] + titles
        for i, vacancy in enumerate(vacancies, start=1):
            row = [i]
            for field in titles:
                cell = ""
                if field in vacancy.__dict__: cell = getattr(vacancy, field)
                elif field in vacancy.salary.__dict__: cell = getattr(vacancy.salary, field)
                row.append(cls._format_cell(cell))

            table.add_row(row)

        table.max_width = 20
        return table

    @staticmethod
    def _format_cell(cell):
        if "\n" in cell:
            cell = ", ".join(cell.split("\n"))
        return cell if len(cell) <= 100 else cell[:100] + "..."


def main():
    # small_vac_50.csv
    dataset = DataSet(input())
    table = Utils.create_table(dataset)
    print(table)


if __name__ == '__main__':
    main()