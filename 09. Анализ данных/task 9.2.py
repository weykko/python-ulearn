import pandas as pd
from collections import Counter


vacancies = pd.read_csv('vacancies_small.csv')

def get_top_skills(vacancies, profession, sort_order):
    filtered_vacancies = vacancies[vacancies['name'].str.contains(profession, case=False, na=False)]
    skills = filtered_vacancies['key_skills'].dropna().str.split('\n').sum()
    skills_freq = Counter(skill.strip() for skill in skills).most_common(5)
    sorted_skills = sorted(skills_freq, key=lambda x: x[1], reverse=sort_order != 'asc')

    return sorted_skills


name = input()
sort_order = input()

result = get_top_skills(vacancies, name, sort_order)
print(result)