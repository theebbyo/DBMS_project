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
        print("1. Sign Up as student")
        print("2. Sign Up as teacher")
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
    sql ="select users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount,  avg(reviews.rating) rating  from users inner join teachers on users.id = teachers.user_id inner join payments on users.id = payments.user_id left join reviews on users.id = reviews.teacher_id group by users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount"
    

    my_db.select_from(sql)
    print("1. For send request")
    print("2. For see others reviews")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        teacherID = int(input("Enter teacher ID: "))
        my_db.insert_into("requests", teacherID, studentID)

    elif choice == 2:
        teacherID = int(input("Enter teacher ID: "))
        sql = f"select u.name, r.rating, r.review from reviews r join users u on r.student_id = u.id where r.teacher_id = {teacherID}"
        my_db.select_from(sql)
    elif choice == 3:
        pass
    else:
        print("Invalid choice")

        
def selection_via_uvinersity(university:str, studentID:int = -1):
    sql =f"select users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount , avg(reviews.rating) rating from users inner join teachers on users.id = teachers.user_id inner join payments on users.id = payments.user_id left join reviews on users.id = reviews.teacher_id where teachers.institution = '{university}' group by users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount"
    my_db.select_from(sql)
    print("1. For send request")
    print("2. For see others reviews")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        teacherID = int(input("Enter teacher ID: "))
        my_db.insert_into("requests", teacherID, studentID)
    elif choice == 2:
        teacherID = int(input("Enter teacher ID: "))
        sql = f"select u.name, r.rating, r.review from reviews r join users u on r.student_id = u.id where r.teacher_id = {teacherID}"
        my_db.select_from(sql)
    elif choice == 3:
        pass
    else:
        print("Invalid choice")

def selection_via_expertize(expertize:str, studentID:int = -1):
    sql = f"select users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount, avg(reviews.rating) rating from users inner join teachers on users.id = teachers.user_id inner join payments on users.id = payments.user_id left join reviews on users.id = reviews.teacher_id where teachers.expertize = '{expertize}' group by users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, payments.amount"
    my_db.select_from(sql)
    
    print("1. For send request")
    print("2. For see others reviews")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        teacherID = int(input("Enter teacher ID: "))
        my_db.insert_into("requests", teacherID, studentID)
    elif choice == 2:
        teacherID = int(input("Enter teacher ID: "))
        sql = f"select u.name, r.rating, r.review from reviews r join users u on r.student_id = u.id where r.teacher_id = {teacherID}"
        my_db.select_from(sql)
    elif choice == 3:
        pass
    else:
        print("Invalid choice")

    

def selectionStudent(studentID:int = -1):
    while True:
        print("1. For select all the teachers")
        print("2. For select teachers from different university")
        print("3. For select teachers from different expertize")
        print("4. For see your teachers")
        print("5. For see your Notifications")
        print("6. Exit")
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
            sql = f"SELECT users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, tuitions.created_at , avg(reviews.rating) rating FROM tuitions INNER JOIN users ON tuitions.teacher_id = users.id INNER JOIN teachers ON tuitions.teacher_id = teachers.user_id LEFT JOIN reviews ON tuitions.teacher_id = reviews.teacher_id WHERE tuitions.student_id = {studentID} GROUP BY users.id, users.name, users.email, users.phone, teachers.institution, teachers.expertize, tuitions.created_at"
            my_db.select_from(sql)
            print("1. For see previous tuition dates")
            print("2. For see pending payments")
            print("3. For chat with teacher")
            print("4. For give rating")
            print("5. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                teacherID = int(input("Enter teacher ID: "))
                sql = f"select td.date from tuitionDates td join tuitions t on td.tuition_id = t.id where t.student_id = {studentID} and t.teacher_id = {teacherID}"
                my_db.select_from(sql)

           
                
            elif choice == 2:
                teacherID = int(input("Enter teacher ID: "))
                sql = f"select p.amount from pendingPayements p join tuitions t on p.tuition_id = t.id where t.student_id = {studentID} and t.teacher_id = {teacherID}"
                my_db.select_from(sql)    
                print("1. For pay")
                print("2. Exit")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    print("hi")
                    my_db.insert_into("makePayements", teacherID, studentID)
                elif choice == 2:
                    pass
                


            elif choice == 3:
                teacherID = int(input("Enter teacher ID: "))
                sql = f"select m.sender, m.message, m.send_at from messages m join tuitions t on m.tuition_id = t.id where t.student_id = {studentID} and t.teacher_id = {teacherID} order by m.send_at"
                my_db.select_from(sql)
                print()
                print("1. For reply")
                print("2. For exit")
                choice = int(input("Enter choice: "))
                while True:
                    if choice == 1:
                        my_db.insert_into("messages", teacherID, studentID)
                        my_db.select_from(sql)
                        print()
                        print("1. For reply")
                        print("2. For exit")
                        choice = int(input("Enter choice: "))

                        
                    elif choice == 2:
                        break
                    else:
                        print("Invalid choice")
                        choice = int(input("Enter choice: "))     
            elif choice == 4:
                teacherID = int(input("Enter teacher ID: "))
                my_db.insert_into("reviews", teacherID, studentID)



            elif choice == 5:
                pass
        
        elif choice == 5:
            toShow = "STUDENT"
            sql = f"select u.name, n.message, n.send_at from notifications n join users u on n.teacher_id = u.id where n.student_id = {studentID} and n.toShow = '{toShow}' order by n.send_at"
            my_db.select_from(sql)
            print()


            
        elif choice == 6:
            break
        else:
            print("Invalid choice")


def selectionTeacher(teacherID:int = -1):
    while True:
        print("1. For see all the requests")
        print("2. For see you students")
        print("3. For see your Notifications")
        print("4. For see your bank account")
        print("5. For see your current ratings")
        print("6. For see reviews")
        print("7. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            sql = f"SELECT users.id, users.name, users.email, users.phone, students.institution, students.address, requests.send_at FROM requests INNER JOIN users ON requests.student_id = users.id INNER JOIN students ON requests.student_id = students.user_id WHERE requests.teacher_id = {teacherID}"
            my_db.select_from(sql)

            print("1. For accept request")
            print("2. For reject request")
            print("3. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                studentID = int(input("Enter student ID: "))
                my_db.insert_into("tuitions", teacherID, studentID,1)
                
            elif choice == 2:
                studentID = int(input("Enter student ID: "))
                my_db.insert_into("tuitions", teacherID, studentID) 
                
            elif choice == 3:
                pass
            else:
                print("Invalid choice")
        elif choice == 2:
            sql = f"SELECT users.id, users.name, users.email, users.phone, students.institution, students.address, tuitions.created_at FROM tuitions INNER JOIN users ON tuitions.student_id = users.id INNER JOIN students ON tuitions.student_id = students.user_id WHERE tuitions.teacher_id = {teacherID}"
            my_db.select_from(sql)
            print("1. For insert tuiton date")
            print("2. For see previous tuition dates")
            print("3. For see pending payments")
            print("4. For chat with student")
            print("5. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                studentID = int(input("Enter student ID: "))
                my_db.insert_into("tuitionDates", teacherID, studentID)
            elif choice == 2:
                studentID = int(input("Enter student ID: "))
                sql = f"select td.date from tuitionDates td join tuitions t on td.tuition_id = t.id where t.student_id = {studentID} and t.teacher_id = {teacherID}"
                my_db.select_from(sql)
                

            elif choice == 3:
                studentID = int(input("Enter student ID: "))
                sql = f"select p.amount from pendingPayements p join tuitions t on p.tuition_id = t.id where t.student_id = {studentID} and t.teacher_id = {teacherID}"
                my_db.select_from(sql)


            elif choice == 4:
                

                studentID = int(input("Enter student ID: "))
                sql = f"select m.sender, m.message, m.send_at from messages m join tuitions t on m.tuition_id = t.id where t.student_id = {studentID} and t.teacher_id = {teacherID} order by m.send_at"
                my_db.select_from(sql)
                print()
                print("1. For reply")
                print("2. For exit")
                choice = int(input("Enter choice: "))
                while True:
                    if choice == 1:
                        my_db.insert_into("messages", teacherID, studentID,1)
                        my_db.select_from(sql)
                        print()
                        print("1. For reply")
                        print("2. For exit")
                        choice = int(input("Enter choice: "))

                        
                    elif choice == 2:
                        break
                    else:
                        print("Invalid choice")
                        choice = int(input("Enter choice: "))


                    




                



            elif choice == 5:
                pass
            else:
                print("Invalid choice")

        elif choice == 3:
            toShow = "TEACHER"
            sql = f"select u.name, n.message, n.send_at from notifications n join users u on n.student_id = u.id where n.teacher_id = {teacherID} and n.toShow = '{toShow}' order by n.send_at"
            my_db.select_from(sql)
            print()
            
        elif choice == 4:
            sql = f"select balance from account where user_id = {teacherID}"
            my_db.select_from(sql)
        
        elif choice == 5:
            sql = f"select avg(rating) rating from reviews where teacher_id = {teacherID}"
            my_db.select_from(sql)

        elif choice == 6:
            sql = f"select u.name, r.rating, r.review from reviews r join users u on r.student_id = u.id where r.teacher_id = {teacherID}"
            my_db.select_from(sql)
        elif choice == 7:
            break
        else:
            print("Invalid choice")







if __name__ == "__main__":
    my_db = MyDbDriver()
    my_db.set_connection()
    
    while True:
        print("1. For Sign up")
        print("2. For Sign in")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            insertion()
        elif choice == 2:
            request:utils.Request
            request = sign_in()
            if request.role == "STUDENT":
                selectionStudent(request.id)
            else:
                selectionTeacher(request.id)
        elif choice == 3:
            break
        else:
            print("Invalid choice")
    
    

    

    my_db.close_connection()
