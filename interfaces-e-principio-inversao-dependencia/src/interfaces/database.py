from abc import ABC, abstractclassmethod

class database(ABC):

    @abstractclassmethod
    def insert():
        raise Exception("Should implement method: insert")

    @abstractclassmethod
    def select():
        raise Exception("Should implement method: select")