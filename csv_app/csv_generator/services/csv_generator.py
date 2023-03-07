from random import randint
import csv
from django.conf import settings
from faker import Faker


def generate_dict_values(schema):
    """
    Function to Select not empty columns values  -> save  names to dict-variable 'csv_columns'
    :return: {'full_name': 'name_column', 'job': 'Jobs_col', 'email': 'mail_col'}
    """
    csv_columns = {}
    my_keys = ['full_name', 'integer_num', 'job', 'email', 'domain_name',
               'phone_number', 'company', 'text', 'address', 'date_fake',
               'min_value_int', 'max_value_int']
    for k, v in schema.__dict__.items():
        if k in my_keys and v:
            csv_columns[k] = v
    # print('csv_columns = ', csv_columns)
    return csv_columns


def generate_row(csv_columns, column_obj) -> list:
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
            row_list.append(randint(column_obj.min_value_int, column_obj.max_value_int + 1))
        if key == 'address':
            row_list.append(fake.address())
        if key == 'date_fake':
            row_list.append(fake.date())
    return row_list


def create_csv(csv_columns, schema, dataset, column_obj):
    # generate row 'Title'  for csv file
    row_title = list(csv_columns.values())
    print('Title row - ', row_title)

    # start to create file
    # file_path = os.path.join(
    #     f"{MEDIA_ROOT}",
    #     f"{schema.name}_R{dataset.rows}.csv",
    # )
    file_path = f'{settings.MEDIA_ROOT}' + f'/{schema.name}_Rows{dataset.rows}.csv'
    dataset.file_download = file_path
    print(file_path)
    dataset.save()
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=schema.separator)
        writer.writerow(row_title)
        for _ in range(int(dataset.rows)):
            # generate one row (with fake data) for csv file
            writer.writerow(generate_row(csv_columns, column_obj))

