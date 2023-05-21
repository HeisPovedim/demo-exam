import mysql.connector

class Connection(object):
    def __init__(self):
        super().__init__()
        
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='demo_exam'
        )
        
        if self.connection.is_connected():
            self.cursor_dict = self.connection.cursor(dictionary=True)
            self.cursor = self.connection.cursor()
        else:
            print("Нет подключения к БД!")
            
    def commit(self):
        """Сделать коммит БД"""
        
        self.connection.commit()
        
    def close(self):
        """Закрыть подключение к БД"""
        
        self.connection.close()