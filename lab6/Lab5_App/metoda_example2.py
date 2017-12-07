import MySQLdb


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.password,
                db = self.db,
                use_unicode=True,
                charset='utf8'
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Test:
    def __init__(self, db_connection, first_name, last_name):
        self.db_connection = db_connection.connection
        self.name = first_name
        self.description = last_name

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO lab5_app_test (first_name, last_name) VALUES (%s, %s);", (self.name, self.description))
        self.db_connection.commit()
        c.close()


class Tests:
    def __init__(self, db_connection):
        self.db_connection = db_connection.connection

    def select_all(self):
        c = self.db_connection.cursor()
        c.execute("SELECT * FROM lab5_app_test;")
        output = c.fetchall()
        c.close()
        return output

    def delete_all(self):
        c = self.db_connection.cursor()
        c.execute("TRUNCATE table lab5_app_test;")
        self.db_connection.commit()
        c.close()


con = Connection('root', '1111', 'mydb')
with con:
    test = Test(con, 'Денис', 'Чечелев')
    test.save()
    tests = Tests(con)#
    select_tests = tests.select_all()
    print(select_tests)
    print('DELETE? 1/0')
    input1 = input()
    if (input1 == '1'):
        tests.delete_all()
    print('---------------------')
    select_tests = tests.select_all()
    print(select_tests)