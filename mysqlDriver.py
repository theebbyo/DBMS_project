import random
import bcrypt
from dbDriver import DbDriver

import mysql.connector

import utils


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



    def insert_into(self, table, teacherID = 1, studentID = 1):
        
        if table == "students":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone = input("Enter phone: ")
            institution = input("Enter institute: ")

            
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
        
        elif table == "teachers":
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            phone = input("Enter phone: ")
            institution = input("Enter institute: ")

            userID = random.randint(1,100000)
            tutorID = random.randint(1,100000)
            paymentID = random.randint(1,100000)
            expertize = input("Enter expertize: ")
            Payment = input("Enter payment: ")
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
            paymentData = {
                "id":paymentID,
                "amount": Payment,
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
                    query = "INSERT INTO payments (id, amount, user_id) VALUES (%(id)s, %(amount)s, %(userID)s)"
                    self.cursor.execute(query, paymentData)
                    self.connection.commit()
                    print("Record inserted successfully into table Payments table")

                except:
                    print("Failed to insert record into table: {}".format(error))
                    
        else:
            id = random.randint(1,100000)
            requestData = {
                "id":id,
                "teacher_id": teacherID,
                "student_id": studentID
            }

            if self.cursor:  
                try:
                    selectQuery = "SELECT * FROM requests WHERE teacher_id = %(teacher_id)s AND student_id = %(student_id)s"
                    self.cursor.execute(selectQuery, requestData)
                    result = self.cursor.fetchone()
                    if result:
                        print("Already requested")
                        return
                    else:
                        query = "INSERT INTO requests (id, teacher_id, student_id) VALUES (%(id)s, %(teacher_id)s, %(student_id)s)"
                        self.cursor.execute(query, requestData)
                        self.connection.commit()
                        print("Record inserted successfully into table Requests table") 
                except mysql.connector.Error as error:
                    print("Failed to insert record into table: {}".format(error))

                
                

    def select_from(self, sql):
        if self.cursor:
            try:
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                
                for row in result:
                    columnNames = [description[0] for description in self.cursor.description]

                    for row in result:
                        for i in range(len(columnNames)):
                            print(f"{columnNames[i]}: {row[i]}")
                        print()

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
                            utils.Request.id = result[0]
                            utils.Request.role = result[5]
                            return utils.Request
                        
                        else:
                            print("Welcome Teacher")
                            utils.Request.id = result[0]
                            utils.Request.role = result[5]
                            return utils.Request
                      
                   
                       
                

               
            except mysql.connector.Error as error:
                print("Failed to select record from table: {}".format(error))
        else:
            print("No active connection")





