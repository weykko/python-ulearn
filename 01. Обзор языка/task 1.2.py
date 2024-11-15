import itertools
import datetime
import enum
import json

exam_tickets_variations = list(map(lambda x: f'{x[0]}, {x[1]}',
                                   itertools.combinations(['1. Overview', '2. Built-in types', '3. Control structures'], 2)))
exam_start_time = datetime.time(12, 00, 00)
exam_start_date = datetime.date(2023, 10, 1)


class Subject(enum.Enum):
    python = 1
    project_practicum = 2
    databases = 3
    history = 4
    pe = 5
    php = 6


exam_data = {
    'tickets': exam_tickets_variations,
    'start': str(exam_start_time) + ' ' + str(exam_start_date),
    'subject': Subject.python.value
}

print(json.dumps(exam_data))