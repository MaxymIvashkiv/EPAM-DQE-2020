import sqlite3, csv, os, datetime, argparse
""""
Щоб запустити код необхідно завантажити tasks.csv та projects.csv з мого гітхабу 
"""

parser = argparse.ArgumentParser(description="Display all tasks for specified project")

parser.add_argument('-xxx', type=str, help="Project name" )

arguments = parser.parse_args()


def varchar_to_date(value: str):
    """
    Перетворює стрічку типу '20200628' на об'єкт типу дата
    :param value: вхідна стрічка у форматі YYYYMMDD
    :return: Обєкт типу дата
    """
    return datetime.date(year=int(value[0:4]), month=int(value[4:6]), day=int(value[6:8]))


def create_database(database_name: str):
    """
    Перевіряє чи файл такої бази існує, ящко так то видаляє і створює новий файл бази
    :param database_name: ім'я бази даних яку хочемо стоврити
    :return: підключену базу даних
    """
    if os.path.exists(f'{database_name}.db'):
        os.remove(f'{database_name}.db')
    return sqlite3.connect(f'{database_name}.db')


def create_table(database_connection, create_statement: str):
    """"
     Створює і одразу комітить таблицю на базі
    :param create_statement: тескт який описує структу таблиці
    """
    cursor = database_connection.cursor()
    cursor.execute(create_statement)
    database_connection.commit()


projects_table = ('CREATE TABLE IF NOT EXISTS Projects ('
                  '   Name TEXT,'
                  '   Description TEXT,'
                  '   Deadline DATE);')

tasks_table = ('CREATE TABLE IF NOT EXISTS Tasks ('
               '    ID NUMBER PRIMARY KEY,'
               '    Priority INTEGER,'
               '    Details TEXT,'
               '    Status TEXT,'
               '    Deadline DATE,'
               '    Completed DATE,'
               '    Project TEXT);')

connection = create_database('Test')

create_table(connection, projects_table)

create_table(connection, tasks_table)

cursor = connection.cursor()

with open('tasks.csv', 'r') as opened_file:
    content = csv.DictReader(opened_file, delimiter='|')
    for row in content:
        ID = int(row['ID'])
        Priority = int(row['Priority'])
        Details = row['Details']
        Status = row['Status']
        Deadline = varchar_to_date(row['Deadline'])
        Completed = varchar_to_date(row['Completed'])
        Project = row['Project']
        cursor.execute('INSERT INTO Tasks(ID, Priority, Details, Status, Deadline, Completed, Project )'
                       'VALUES (?, ?, ?, ?, ?, ?, ?)', (ID, Priority, Details, Status, Deadline, Completed, Project))
        connection.commit()

with open('projects.csv', 'r') as opened_file:
    content = csv.DictReader(opened_file, delimiter='|')
    for row in content:
        Name = row['Name']
        Description = row['Description']
        Deadline = varchar_to_date(row['Deadline'])
        cursor.execute('INSERT INTO projects (Name, Description, Deadline)'
                       'VALUES (?, ?, ?)', (Name, Description, Deadline))
        connection.commit()


#xxx = 'Yorkton' - Тестове ім'я проекту

answer_set = connection.execute(f'SELECT * FROM tasks WHERE Project = "{arguments.xxx}"').fetchall()
for row in answer_set:
    print(row)
