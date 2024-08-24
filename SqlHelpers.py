#MySQL_Helpers

from app import mysql, session

class Table():
    def __init__(self, table_name):
        self.table_name = table_name
