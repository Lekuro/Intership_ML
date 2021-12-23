import sqlite3
from funcs import get_data_from_file, write_data_csv
from funcs import read_from_db, add_row_to_db, update_row, delete_row


data = get_data_from_file('data.txt')
write_data_csv(data, 'from_file')
# create DB
con = sqlite3.connect('world_city.db')
cur = con.cursor()
sql = '''
CREATE TABLE city (
    id_city INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    name_city TEXT
);
'''
try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print('executescript error: ', err)
else:
    print('Table City is created.')
# fill DB
sql = '''
INSERT INTO city (id_city,country,name_city) VALUES(?,?,?)
'''
try:
    cur.executemany(sql, data)
except sqlite3.DatabaseError as err:
    print('executemany error: ', err)
else:
    print('Table City filled')
    con.commit()
# close DB
cur.close()
con.close()

# result_db = read_from_db('world_city.db')
# write_data_csv(result_db, 'from_db')
# add_row_to_db('world_city.db', ('Ukraine', 'Osa'))
# result_db = read_from_db('world_city.db')
# write_data_csv(result_db, 'added_row_db')
update_row('world_city.db', ('Ukraine', 'Odesa', 3033))
result_db = read_from_db('world_city.db')
write_data_csv(result_db, 'updated_row_db')
# delete_row('world_city.db', 3031)
# result_db = read_from_db('world_city.db')
# write_data_csv(result_db, 'deleted_row_db')
