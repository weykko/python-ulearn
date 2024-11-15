import json
import bs4
import re

exchange = {
    '₽': 1.0,
    '$': 100.0,
    '€': 105.0,
    '₸': 0.210,
    'Br': 30.0,
}

result = {
    'vacancy': None,
    'salary': None,
    'experience': None,
    'company': None,
    'description': None,
    'skills': None,
    'created_at': None,
}

def parse_vacancy_html(file_name, result):
    with open(file_name) as f:
        page = bs4.BeautifulSoup(f, "html.parser")

    result["vacancy"] = page.find(attrs={"data-qa": "vacancy-title"}).text

    salary_tag = page.find(attrs={"data-qa": "vacancy-salary"}).text
    salary = re.findall(r"\d{1,3}(?:\s\d{3})*", salary_tag)
    currency = re.findall(r"[₽$€₸]|Br", salary_tag)[0]
    result["salary"] = "->".join(str(float(s.replace("\xa0", "")) * exchange[currency]) for s in salary)

    experience_tag = page.find(attrs={"data-qa": "vacancy-experience"}).text
    experience_years = [e for e in experience_tag if e.isdigit()]
    if experience_years: result["experience"] = "-".join(experience_years)

    result["company"] = page.find(attrs={"data-qa": "vacancy-company-name"}).text

    result["description"] = page.find(attrs={"data-qa": "vacancy-description"}).text

    skills_tag = page.find_all(attrs={"data-qa": "bloko-tag bloko-tag_inline skills-element"})
    result["skills"] = "; ".join(s.text for s in skills_tag)

    result["created_at"] = page.find(class_="vacancy-creation-time-redesigned").find("span").text.replace("\xa0", " ")

    print(json.dumps(result))


html = input()
parse_vacancy_html(html, result)