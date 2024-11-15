import csv
import re

def format_time(text): return re.sub(r"(\d{2})\.(\d{2})(?!%)", r"\1:\2", text)

def remove_html_tags(text): return re.sub(r"<.*?>", "", text)

def format_datetime(text):
    return re.sub(r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})\+\d{4}", r"\4:\5:\6 \3/\2/\1", text)

def highlight_keywords(text, keywords):
    for keyword in keywords:
        p = re.compile(r'\b([A-Za-zА-Яа-яёЁ0-9]*' + keyword + r'[A-Za-zА-Яа-яёЁ0-9]*)\b', re.IGNORECASE)
        text = p.sub(lambda match: match.group(0).upper(), text)
    return text

def format_csv(input_file, output_file, keywords):
    keywords_list = [w for w in keywords.split(",")]

    with open(input_file, mode="r", encoding="utf-8") as infile, \
         open(output_file, mode="w", encoding="utf-8") as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            format_row = []
            for str in row:
                str = format_time(str)
                str = remove_html_tags(str)
                str = format_datetime(str)
                str = highlight_keywords(str, keywords_list)
                format_row.append(str)

            writer.writerow(format_row)


file = input()
new_file = input()
highlight = input()

format_csv(file, new_file, highlight)