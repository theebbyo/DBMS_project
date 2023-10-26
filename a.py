from mysqlDriver import MyDbDriver



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



def selecion_all_teachers():
    sql = "SELECT users.name, users.email, users.phone, teachers.institution, teachers.expertize, offline_payments.amount, online_payments.amount FROM users INNER JOIN teachers ON users.id = teachers.user_id inner JOIN offline_payments ON users.id = offline_payments.user_id inner join online_payments ON users.id = online_payments.user_id"
    my_db.select_from(sql)

def selection_via_uvinersity(university:str):
    sql = f"SELECT users.name, users.email, users.phone, teachers.institution, teachers.expertize, offline_payments.amount, online_payments.amount FROM users INNER JOIN teachers ON users.id = teachers.user_id inner JOIN offline_payments ON users.id = offline_payments.user_id inner join online_payments ON users.id = online_payments.user_id WHERE teachers.institution = '{university}'"
    my_db.select_from(sql)

def selection_via_expertize(expertize:str):
    sql = f"SELECT users.name, users.email, users.phone, teachers.institution, teachers.expertize, offline_payments.amount, online_payments.amount FROM users INNER JOIN teachers ON users.id = teachers.user_id inner JOIN offline_payments ON users.id = offline_payments.user_id inner join online_payments ON users.id = online_payments.user_id WHERE teachers.expertize = '{expertize}'"
    my_db.select_from(sql)

def selection():
    while True:
        print("1. For select all the teachers")
        print("2. For select teachers from different university")
        print("3. For select teachers from different expertize")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            selecion_all_teachers()
        elif choice == 2:
                    while True:
                        print("1. For select teachers from BUET")
                        print("2. For select teachers from Dhaka University")
                        print("3. For select teachers from Dhaka Medical College")
                        print("4. Exit")
                        choice = int(input("Enter choice: "))
                        if choice == 1:
                            selection_via_uvinersity("BUET")
                        elif choice == 2:
                            selection_via_uvinersity("Dhaka University")

                        elif choice == 3:
                            selection_via_uvinersity("Dhaka Medical College")
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
                    selection_via_expertize("Math")
                elif choice == 2:
                    selection_via_expertize("Physics")

                elif choice == 3:
                    selection_via_expertize("Chemistry")
                elif choice == 4:
                    selection_via_expertize("Biology")
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
            selection()
                

        elif choice == 3:
            break
        else:
            print("Invalid choice")
    
    

    

    my_db.close_connection()
