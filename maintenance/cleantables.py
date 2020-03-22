
import sqlite3
db = sqlite3.connect("db.sqlite3")
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
tables = cursor.fetchall()
names = []
for table_name in tables:
    table_name = table_name[0]
    if table_name.startswith('auth_') : continue
    if table_name.startswith('django_') : continue
    if table_name.startswith('social_') : continue
    if table_name.startswith('sqlite_') : continue
    names.append(table_name)

todelete = []
for table_name in names:
    cursor.execute("SELECT count(*) FROM "+table_name+';')
    row = cursor.fetchone()
    count = row[0]
    print(table_name, count);
    if count < 1 : continue
    sql = 'DELETE FROM '+table_name+';'
    print(sql)
    cursor.execute(sql)
    db.commit()

cursor.close()
db.close()


