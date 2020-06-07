import argparse, csv, json

parser = argparse.ArgumentParser(description="Convert csv file to json.")

parser.add_argument("-csv", type=str, help="Path to csv",)

parser.add_argument("-json", type=str, help="<Path and name of JSON file")

arguments = parser.parse_args()

data = {}

with open(arguments.csv, 'r') as opened_csv_file:
    content = csv.DictReader(opened_csv_file)
    field_names = [name for name in content.fieldnames if name != 'password']
    for row in content:
        # Формую словник зі всіма значеннями окрім паролю
        # Поля посортовані у алфавітному порядку як у прикладі на пошті
        # Записую вкладений словник де user_id - key, а value - словник для кожного рядка включно з user_id,
        # результатом є словник зі словників :)
        data_row = {}
        for field in sorted(field_names):
            data_row[field] = row[field]
        data[row["user_id"]] = data_row

with open(arguments.json, 'w') as json_file:
    # Записую у json файл лише value  для кожного user_id
    for key in data:
        json_file.write(json.dumps(data[key], indent=4))
        json_file.write('\n')
