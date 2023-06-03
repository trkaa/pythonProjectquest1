import sqlite3


class DataBase:

    def __init__(self, db_path: str = 'data_base/db_bot.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):

        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_check_points(self):
        sql = '''CREATE TABLE IF NOT EXISTS check_points (id_player INTEGER PRIMARY KEY AUTOINCREMENT ,telegram_id 
        INTEGER , name VARCHAR, intro_checkpoint VARCHAR, point1 VARCHAR, point2 VARCHAR, point3 VARCHAR, 
        point4 VARCHAR, point5 VARCHAR, point6 VARCHAR, point7 VARCHAR, point8 VARCHAR, point9 VARCHAR, 
        point10 VARCHAR, point11 VARCHAR, point12 VARCHAR, point13 VARCHAR, point14 VARCHAR, user_state VARCHAR) '''
        self.execute(sql, commit=True)

    def new_user(self, user_tuple: tuple):
        sql = '''INSERT INTO check_points (telegram_id, name) VALUES (?, ?)'''
        self.execute(sql, user_tuple, commit=True)

    def user_exist(self, user_id: int):
        parameters = (user_id,)
        sql = '''SELECT name FROM check_points WHERE telegram_id=?'''
        return self.execute(sql, parameters, fetchone=True)

    def get_users(self):
        sql = '''SELECT telegram_id FROM check_points'''
        return self.execute(sql, fetchall=True)

    def point_time(self, point: str, user_time: tuple):
        sql = f'''UPDATE check_points SET {point}=? WHERE telegram_id=? '''
        self.execute(sql, user_time, commit=True)



    def user_state(self, current_state: tuple):
        sql = '''UPDATE check_points SET user_state=? WHERE telegram_id=? '''
        self.execute(sql, current_state, commit=True)


    def load_state(self, user_id: int):
        parameters = (user_id,)
        sql = '''SELECT user_state FROM check_points WHERE telegram_id=?'''
        return self.execute(sql, parameters, fetchone=True)

