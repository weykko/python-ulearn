import pandas as pd

vacancies = pd.read_csv('vacancies_for_learn_demo.csv')


def analyze_vacancies(vacancies, prof):
    vacancies = vacancies[vacancies['salary_currency'] == 'RUR'].copy()
    vacancies['year'] = pd.to_datetime(vacancies['published_at']).dt.year
    max_year = vacancies['year'].max()
    vacancies = vacancies[vacancies['year'] > max_year - 5]
    years = vacancies['year'].unique()

    vacancies['average_salary'] = vacancies[['salary_from', 'salary_to']].mean(axis=1)
    prof_vacancies = vacancies[vacancies['name'].str.contains(prof, na=False)]

    salary_by_year = (
        vacancies
        .groupby('year')['average_salary']
        .mean()
        .round(1)
        .astype(int)
        .to_dict()
    )

    count_by_year = (
        vacancies['year']
        .value_counts(sort=False)
        .to_dict()
    )

    prof_salary_by_year = (
        prof_vacancies
        .groupby('year')['average_salary']
        .mean()
        .round(1)
        .astype(int)
        .reindex(years, fill_value=0)
        .to_dict()
    )

    prof_count_by_year = (
        prof_vacancies['year']
        .value_counts(sort=False)
        .reindex(years, fill_value=0)
        .to_dict()
    )

    city_salary = (
        prof_vacancies
        .groupby('area_name')['average_salary']
        .mean()
        .round(1)
        .astype(int)
        .sort_index()
        .sort_values(ascending=False, kind='stable')
        .head(10)
        .to_dict()
    )

    city_vacancy_share = (
        prof_vacancies['area_name']
        .value_counts(normalize=True, sort=False)
        .where(lambda x: x >= 0.01)
        .round(4)
        .sort_index()
        .sort_values(ascending=False, kind='stable')
        .head(10)
        .to_dict()
    )

    return {
        'Динамика уровня зарплат по годам': salary_by_year,
        'Динамика количества вакансий по годам': count_by_year,
        'Динамика уровня зарплат по годам для выбранной профессии': prof_salary_by_year,
        'Динамика количества вакансий по годам для выбранной профессии': prof_count_by_year,
        'Уровень зарплат по городам для выбранной профессии (в порядке убывания)': city_salary,
        'Доля вакансий по городам для выбранной профессии (в порядке убывания)': city_vacancy_share
    }


name = input()
result = analyze_vacancies(vacancies, name)

for key, value in result.items():
    print(f'{key}: {value}')