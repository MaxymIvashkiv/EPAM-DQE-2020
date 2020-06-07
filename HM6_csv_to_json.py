
parser = argparse.ArgumentParser(description="Convert csv file to json.")

parser.add_argument("-csv", type=str, help="Path to csv",)


arguments = parser.parse_args()

path = os.path.split(arguments.json)[0]

file_name = os.path.split(arguments.json)[1]

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

while True:
    try:
        with open(path + '\\' + file_name, 'w') as json_file:
            # Записую у json файл лише value  для кожного user_id
            for key in data:
                json_file.write(json.dumps(data[key], indent=4))
                json_file.write('\n')
    except FileNotFoundError:
        # створює нову папку якщо такої не існує
        os.mkdir(path)
    else:
        break
