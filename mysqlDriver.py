import random
import bcrypt
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
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        phone = input("Enter phone: ")
        institution = input("Enter institute: ")

        if table == "students":
            
            address = input("Enter address: ")
            userID = random.randint(1,100000)
            studentID = random.randint(1,100000)
            userData = {
                "id":userID,
                "name": name,
                "email": email,
                "password": bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()),
                "phone": phone,
                "role": "STUDENT"
                }
            
            studentData = {
                "id":studentID,
                "institution": institution,
                "address": address,
                "userID": userID
            }
            
            if self.cursor:
                try:
                    query = "INSERT INTO users (id, name, email, password, phone, role) VALUES (%(id)s, %(name)s, %(email)s, %(password)s, %(phone)s, %(role)s)"
                    self.cursor.execute(query, userData)
                    self.connection.commit()
                    print("Record inserted successfully into table Users table")
                except mysql.connector.Error as error:
                    print("Failed to insert record into table: {}".format(error))
                
                try:
                    query = "INSERT INTO students (id, institution, address, user_id) VALUES (%(id)s, %(institution)s, %(address)s, %(userID)s)"
                    self.cursor.execute(query, studentData)
                    self.connection.commit()
                    print("Record inserted successfully into table Students table")

                except:
                    print("Failed to insert record into table: {}".format(error))
        
        else:
            userID = random.randint(1,100000)
            tutorID = random.randint(1,100000)
            paymentID = random.randint(1,100000)
            expertize = input("Enter expertize: ")
            offlinePayment = input("Enter offline payment: ")
            onlinePayment = input("Enter online payment: ")
            userData = {
                "id":userID,
                "name": name,
                "email": email,
                "password": bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()),
                "phone": phone,
                "role": "TEACHER"
                }
            
            tutorData = {
                "id":tutorID,
                "institution": institution,
                "userID": userID,
                "expertize":expertize
            }
            offlinepaymentData = {
                "id":paymentID,
                "amount": offlinePayment,
                "userID": userID
                
            }
            onlinePaymentData = {
                "id":paymentID,
                "amount": onlinePayment,
                "userID": userID
                
            }
            
            if self.cursor:
                try:
                    query = "INSERT INTO users (id, name, email, password, phone, role) VALUES (%(id)s, %(name)s, %(email)s, %(password)s, %(phone)s, %(role)s)"
                    self.cursor.execute(query, userData)
                    self.connection.commit()
                    print("Record inserted successfully into table Users table")
                except mysql.connector.Error as error:
                    print("Failed to insert record into table: {}".format(error))
                
                try:
                    query = "INSERT INTO teachers (id, institution, user_id, expertize) VALUES (%(id)s, %(institution)s, %(userID)s, %(expertize)s)"
                    self.cursor.execute(query, tutorData)
                    self.connection.commit()
                    print("Record inserted successfully into table Teachers table")

                except:
                    print("Failed to insert record into table: {}".format(error))
                

                try:
                    query = "INSERT INTO offline_payments (id, amount, user_id) VALUES (%(id)s, %(amount)s, %(userID)s)"
                    self.cursor.execute(query, offlinepaymentData)
                    self.connection.commit()
                    print("Record inserted successfully into table Offline Payments table")

                except:
                    print("Failed to insert record into table: {}".format(error))

                try:
                    query = "INSERT INTO  online_payments (id, amount, user_id) VALUES (%(id)s, %(amount)s, %(userID)s)"
                    self.cursor.execute(query, onlinePaymentData)
                    self.connection.commit()
                    print("Record inserted successfully into table Online Payments table")

                except:
                    print("Failed to insert record into table: {}".format(error))        

            
                
                

    def select_from(self, sql):
        if self.cursor:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                
                for row in result:
                    print(row)

            except mysql.connector.Error as error:
                print("Failed to select record from table: {}".format(error))
        
        else:
            print("No active connection")


    def login(self, email, password):
        if self.cursor:
            try:
                query = "SELECT * FROM users WHERE email = %(email)s"
                self.cursor.execute(query, {"email": email})
                result = self.cursor.fetchone()

               

                if result:
                    if bcrypt.checkpw(password.encode('utf-8'), result[3].encode('utf-8')):
                        if result[5] == "STUDENT":
                            print("Welcome Student")
                            return result[5]
                        
                        else:
                            print("Welcome Teacher")
                            return result[5]
                      
                   
                       
                

               
            except mysql.connector.Error as error:
                print("Failed to select record from table: {}".format(error))
        else:
            print("No active connection")




