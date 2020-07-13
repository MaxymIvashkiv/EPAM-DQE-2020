from pymongo import MongoClient
import sqlite3
"""
перед запуском коду скачати файл бази даних sqlite3 - sqlite3_data.db
"""

def move_table_from_sqlite_to_mongo(sqlite_db, sqlite_table: str, mongo_db, mongo_table: str):
    """
    1. Зчитує схему таблиці назва_колонки: порядок колонки у таблиці
    2. У результуючому рядку співставляє стовпець з відповідним йому значенням

    :param sqlite_db: підключена файл бази даних sqlite3
    :param sqlite_table: назва таблиці у sqlite3
    :param mongo_db: підключений MongoDB база
    :param mongo_table: нова колекція
    :return: переносить по одному рядку дані з sqlite3 таблиці у колекцію MongoDB
    """
    column_names = {}
    for row in sqlite_db.execute(f'SELECT name, cid FROM PRAGMA_TABLE_INFO("{sqlite_table}");'):
        column_names[row[0]] = row[1]

    answer_set = sqlite_db.execute(f'SELECT * FROM {sqlite_table};').fetchall()
    for row in answer_set:
        stage_dict = {}
        for key, value in column_names.items():
            stage_dict[key] = row[value]
        mongo_db[mongo_table].insert_one(stage_dict)


sqlite3_connection = sqlite3.connect("sqlite3_data.db")

mongo_client = MongoClient(host='localhost', port=27017)

# MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")

mongo_database = mongo_client["New_Mongo_DB"]

move_table_from_sqlite_to_mongo(sqlite3_connection, 'Tasks', mongo_database, 'Tasks')

move_table_from_sqlite_to_mongo(sqlite3_connection, 'Projects', mongo_database, 'Projects')

condition = {'Status': 'canceled'}

projects_list = [i['Project'] for i in mongo_database['Tasks'].find(condition)]
for i in set(projects_list):
    print(i)


