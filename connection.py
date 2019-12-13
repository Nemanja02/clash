import mysql.connector

class connection:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="clash"
        )
    def addUser(self, token):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO users (access_token) VALUES ("{0}")'.format(token))
        self.db.commit()
    def getUserData(self, token):
        cursor = self.db.cursor()
        cursor.execute('SELECT level,exp,gold,elixir,gems,username,trophies FROM users WHERE access_token = "{0}"'.format(token))
        result = cursor.fetchall()
        return result

