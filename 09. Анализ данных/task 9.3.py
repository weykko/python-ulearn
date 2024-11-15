import pandas as pd

vacancies = pd.read_csv('vacancies_small.csv')


def get_city_salary_stats(vacancies):
    filtered_vacancies = vacancies[vacancies['salary_currency'] == 'RUR'].copy()
    filtered_vacancies['average_salary'] = filtered_vacancies[['salary_from', 'salary_to']].mean(axis=1)

    city_salary = (
        filtered_vacancies
        .groupby('area_name')['average_salary']
        .mean()
        .dropna()
        .round()
        .astype(int)
        .sort_index()
        .sort_values(ascending=False, kind='stable')
        .to_dict()
    )

    return city_salary


result = get_city_salary_stats(vacancies)
print(result)
