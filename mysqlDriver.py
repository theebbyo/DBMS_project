from dbDriver import DbDriver

import mysql.connector


class MyDbDriver(DbDriver):
    def set_connection(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='tuition'
        )
        
        if self.connection.is_connected():
            print("Connected to the database")
            self.cursor = self.connection.cursor()
    
    def close_connection(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.connection.close()
            print("Connection to the database closed")
        else:
            print("No active connection to close")



    def insert_into(self, table):
        # Implementation for inserting data into a table
        pass

    def select_from(self, sql):
        # Implementation for executing a SELECT query
        pass




