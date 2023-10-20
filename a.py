from mysqlDriver import MyDbDriver





if __name__ == "__main__":
    my_db = MyDbDriver()
    my_db.set_connection()
    my_db.insert_into("teachers")
    my_db.close_connection()