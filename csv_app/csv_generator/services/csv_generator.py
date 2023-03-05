import os
from pathlib import Path
from random import randint
import csv

from faker import Faker

def generate_row(csv_columns, schema) -> list:
    fake = Faker()
    # Example : csv_columns {'full_name': 'name_for', 'job': 'job_col'}
    row_list = []
    for key in csv_columns.keys():
        if key == 'full_name':
            row_list.append(fake.name())
        if key == 'job':
            row_list.append(fake.job())
        if key == 'email':
            row_list.append(fake.email())
        if key == 'domain_name':
            row_list.append(fake.domain_name())
        if key == 'phone_number':
            row_list.append(fake.phone_number())
        if key == 'company':
            row_list.append(fake.company())
        if key == 'text':
            row_list.append(fake.text(max_nb_chars=30))
        if key == 'integer_num':
            row_list.append(randint(schema.min_value_int, schema.max_value_int + 1))
        if key == 'address':
            row_list.append(fake.address())
        if key == 'date_fake':
            row_list.append(fake.date())
    return row_list


def create_csv(csv_columns, schema, rows_count):
    # generate row 'Title'  for csv file
    row_title = list(csv_columns.values())
    print('Title row - ', row_title)

    # start to create file
    MEDIA_ROOT = Path(__file__).resolve().parent.parent / 'media'
    file_path = os.path.join(
        f"{MEDIA_ROOT}",
        f"{schema.name}.csv",
    )
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=schema.separator)
        writer.writerow(row_title)
        for _ in range(int(rows_count)):
            # generate one row (with fake data) for csv file
            writer.writerow(generate_row(csv_columns, schema))
        print('OK')
