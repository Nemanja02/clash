import os, sys
import configparser
from os import path
import secrets
from connection import connection

class user:
    def __init__(self, token):
        self.token = token
    def addUser(self):
        conn = connection()
        conn.addUser(self.token)
    def getUserData(self):
        conn = connection()
        return conn.getUserData(self.token)


class loader:
    def __init__(self):
        if (path.exists('cache/settings.conf') == False):
            os.mkdir('cache')
            config = configparser.ConfigParser()
            self.token = secrets.token_hex(32)
            config['DEFAULT'] = {'ACCESS_TOKEN': self.token}
            with open('cache/settings.conf', 'w') as configfile:
                config.write(configfile)
            u = user(self.token)
            u.addUser()
            
        else:
            config = configparser.ConfigParser()
            config.read('cache/settings.conf')
            self.token = config['DEFAULT']['ACCESS_TOKEN']

    def getAccessToken(self):
        return self.token


    def getUserData(self):
        u = user(self.token)
        return u.getUserData()[0]
        
        