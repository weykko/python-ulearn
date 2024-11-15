import pandas as pd


vacancies = pd.read_csv('vacancies_small.csv')

def filter_sort_vacancies(vacancies, column, key, sort_by, sort_order):
    filtered_vacancies = vacancies[vacancies[column].str.contains(key, case=False, na=False)]
    sorted_vacancies = filtered_vacancies.sort_values(by=sort_by, ascending=sort_order == 'asc', kind='stable')

    return sorted_vacancies['name'].tolist()


column = input()
key = input()
sort_by = input()
sort_order = input()

result = filter_sort_vacancies(vacancies, column, key, sort_by, sort_order)
print(result)