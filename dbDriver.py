from abc import ABC, abstractmethod

class DbDriver(ABC):
    @abstractmethod
    def set_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def insert_into(self, table):
        pass

    @abstractmethod
    def select_from(self, sql):
        pass
