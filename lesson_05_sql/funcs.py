import csv
import sqlite3
from sqlite3.dbapi2 import DatabaseError


def get_data_from_file(file_name):
    with open(f'lesson_05_sql/{file_name}', 'r')as file:
        file_list = file.readlines()
    file_list = [i[:-1] if i[-1] == '\n' else i for i in file_list]
    file_list = [i.split(';') for i in file_list]
    titles = file_list[0]
    # print(titles)
    file_list = file_list[1:]
    file_list = [[int(i[2][1:-1]), str(i[0][1:-1]), str(i[1][1:-1])]
                 for i in file_list]
    # for item in file_list:
    #     item[2] = int(item[2][1:-1])
    file_list = sorted(file_list, key=lambda x: x[0])
    # print(type(file_list))
    # print(file_list)
    return file_list


def write_data_csv(data, file_name):
    with open(f'lesson_05_sql/{file_name}.csv', 'w')as f_csv:
        csv_writer = csv.writer(f_csv, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["id", "country", "city"])
        for item in data:
            csv_writer.writerow(item)


def read_from_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    try:
        cur.execute("SELECT * FROM city")
        # cur.fetchall()
    except sqlite3.DatabaseError as err:
        print('read err: ', err)
    else:
        print('readed')
    result_db = []
    # for id, country, city in cur:
    # result_db.append([id, country, city])
    for row in cur:
        if row:
            result_db.append(row)
        # print('row', row)
    cur.close()
    con.close()
    return result_db


def add_row_to_db(db_name, data):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    if isinstance(data, tuple):
        sql = f'''
        INSERT INTO city (country,name_city) VALUES {data};
        '''
        try:
            cur.execute(sql)
        except sqlite3.DatabaseError as err:
            print('add row err: ', err.args)
        else:
            print('added new row')
            con.commit()
    cur.close()
    con.close()


def update_row(db_name, data):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    if isinstance(data, tuple):
        sql = f''' 
        UPDATE city SET country = ? , name_city = ? WHERE id_city = ?
        '''
        try:
            cur.execute(sql, data)
        except sqlite3.DatabaseError as err:
            print('updated row err: ', err.args)
        else:
            print('updated row')
            con.commit()
    cur.close()
    con.close()


def delete_row(db_name, id):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    sql = f''' 
    DELETE FROM city WHERE id_city = ?
    '''
    try:
        cur.execute(sql, (id,))
    except sqlite3.DatabaseError as err:
        print('deleted row err: ', err.args)
    else:
        print('deleted row')
        con.commit()
    cur.close()
    con.close()
