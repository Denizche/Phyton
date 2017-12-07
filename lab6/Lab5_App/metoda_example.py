import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='1111',
    db='mydb',
    use_unicode=True,
    charset='utf8'
)

c = db.cursor()

c.execute("INSERT INTO lab5_app_test (first_name, last_name) VALUES (%s, %s);", ('Денис', 'Чечелев'))
db.commit()

c.execute("SELECT * FROM lab5_app_test;")
tests = c.fetchall()
for test in tests:
    print(test)

#c.execute("DELETE FROM Test;")
#db.commit()

#c.execute("SELECT * FROM Test;")
#tests = c.fetchall()
#print('БД после удаления:')
#for test in tests:
#    print(test)

c.close()
db.close()
