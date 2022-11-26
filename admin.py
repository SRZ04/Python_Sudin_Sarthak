import sqlite3
conn=sqlite3.connect(".\doctor\drDetailsFile.db")
drCursor=conn.cursor()

connect=sqlite3.connect(".\doctor\ptDetailsFile.db")
ptCursor=connect.cursor()


class Doctor:
    def __init__(self):
        pass

    def showDrDetails():
        select_cmd= '''SELECT * FROM drDetailsTable'''
        result=drCursor.execute(select_cmd)
        print("*"*20)
        print("YOUR RECORD")
        for data in result:        
            print(f"Name: {data[0]}")
            print(f"Contact: {data[1]}")
            print(f"Degree: {data[2]}")
            print(f"Experience year: {data[3]}")
            print(f"Availability: {data[4]}")
        conn.commit
    
class Patient:
    def __init__(self):
        pass
    
    def showptDetails():
        select_cmd= '''SELECT * FROM ptDetailsTable'''
        result=ptCursor.execute(select_cmd)
        print("*"*20)
        print("YOUR RECORD")
        for data in result:        
            print(f"Name: {data[0]}")
            print(f"Age: {data[1]}")
            print(f"Gender: {data[2]}")
            print(f"Emergency: {data[3]}")
        conn.commit

class Admin(Doctor,Patient):
        def __init__(self):
            pass
        
        def Check():
            var=int(input("Enter 1 for dr and 2 for patient: "))
            if(var==1):
                Doctor.showDrDetails()
            if(var==2):
                Patient.showptDetails()


                
# Admin.Check()

