import json
import re

def format_description(value):
    sentences = value.split(". ")
    return ". ".join(sentence.capitalize() for sentence in sentences)

def format_salary(value): return format(round(float(value), 2), ".2f")

def format_key_phrase(value): return f"{value.upper()}!"

def format_addition(value): return f"..{value.lower()}.."

def format_company_info(value): return re.sub(r"\(.+\)|\)|\(", "  ", value)

def format_key_skills(value): return value.replace("&nbsp", " ")

format_functions = {
    "description": format_description,
    "salary": format_salary,
    "key_phrase": format_key_phrase,
    "addition": format_addition,
    "company_info": format_company_info,
    "key_skills": format_key_skills
}

text = input()
headings = input()
result = {}

fields = text[:-1].split("; ")
for field in fields:
    key, value = field.split(": ")
    key = key.strip()
    if key in headings:
        result[key] = format_functions[key](value)

print(json.dumps(result))