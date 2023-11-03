import bcrypt
from mysqlDriver import MyDbDriver
import utils



request:utils.Request



def sign_in():
    email = input("Enter email: ")
    password = input("Enter password: ")
    while True:
        request = my_db.login(email, password)
        if request.role == "TEACHER" or request.role == "STUDENT":
            print("Login successfull")
            return request
        else:
            print("Invalid email or password")
            email = input("Enter email: ")
            password = input("Enter password: ")

    
    



def insertion():
    while True:
        print("1. Insert into students")
        print("2. Insert into teachers")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            my_db.insert_into("students")
        elif choice == 2:
            my_db.insert_into("teachers")
        elif choice == 3:
            break
        else:
            print("Invalid choice")




def selecion_all_teachers(studentID:int=-1):
    

    sql = "SELECT users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount FROM users INNER JOIN teachers ON users.id = teachers.user_id inner JOIN payments ON users.id = payments.user_id "
    my_db.select_from(sql)
    print("1. For send request")
    print("2. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        teacherID = int(input("Enter teacher ID: "))
        my_db.insert_into("requests", teacherID, studentID)
    elif choice == 2:
        pass
    else:
        print("Invalid choice")

        
def selection_via_uvinersity(university:str, studentID:int = -1):
    sql = f"SELECT users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount FROM users INNER JOIN teachers ON users.id = teachers.user_id inner JOIN payments ON users.id = payments.user_id WHERE teachers.institution = '{university}'"
    my_db.select_from(sql)
    print("1. For send request")
    print("2. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        teacherID = int(input("Enter teacher ID: "))
        my_db.insert_into("requests", teacherID, studentID)
    elif choice == 2:
        pass
    else:
        print("Invalid choice")

def selection_via_expertize(expertize:str, studentID:int = -1):
    sql = f"SELECT users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount FROM users INNER JOIN teachers ON users.id = teachers.user_id inner JOIN payments ON users.id = payments.user_id  WHERE teachers.expertize = '{expertize}'"
    my_db.select_from(sql)
    
    print("1. For send request")
    print("2. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        teacherID = int(input("Enter teacher ID: "))
        my_db.insert_into("requests", teacherID, studentID)
    elif choice == 2:
        pass
    else:
        print("Invalid choice")

    

def selection(studentID:int = -1):
    while True:
        print("1. For select all the teachers")
        print("2. For select teachers from different university")
        print("3. For select teachers from different expertize")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            selecion_all_teachers(studentID)
        elif choice == 2:
                    while True:
                        print("1. For select teachers from BUET")
                        print("2. For select teachers from Dhaka University")
                        print("3. For select teachers from Dhaka Medical College")
                        print("4. Exit")
                        choice = int(input("Enter choice: "))
                        if choice == 1:
                            selection_via_uvinersity("BUET", studentID)

                        elif choice == 2:
                            selection_via_uvinersity("Dhaka University", studentID)

                        elif choice == 3:
                            selection_via_uvinersity("Dhaka Medical College", studentID)
                        elif choice == 4:
                            break
                        else:
                            print("Invalid choice")
        

        elif choice == 3:
            while True:
                print("1. For select teachers from Math")
                print("2. For select teachers from Physics")
                print("3. For select teachers from Chemistry")
                print("4. For select teachers from Biology")
                print("5. Exit")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    selection_via_expertize("Math", studentID)
                elif choice == 2:
                    selection_via_expertize("Physics", studentID)

                elif choice == 3:
                    selection_via_expertize("Chemistry", studentID)
                elif choice == 4:
                    selection_via_expertize("Biology", studentID)
                elif choice == 5:
                    break
                else:
                    print("Invalid choice")
        elif choice == 4:
            break

if __name__ == "__main__":
    my_db = MyDbDriver()
    my_db.set_connection()
    
    while True:
        print("1. For insertion operation")
        print("2. For selection operation")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            insertion()
        elif choice == 2:
            request:utils.Request
            request = sign_in()
            if request.role == "STUDENT":
                selection(request.id)
            else:
                print("You are not a student")

        elif choice == 3:
            break
        else:
            print("Invalid choice")
    
    

    

    my_db.close_connection()
