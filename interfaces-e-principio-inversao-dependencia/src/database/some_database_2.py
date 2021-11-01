from src.interfaces import database

class Database2(database):

    def insert(self):
        print("Inserting Something")

    def select(self):
        print("Selecting Something")