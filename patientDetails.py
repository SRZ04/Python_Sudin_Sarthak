def patientDetailsFunction():
    import sqlite3
    conn=sqlite3.connect(".\doctor\ptDetailsFile.db")
    patientCursor=conn.cursor()

    connect=sqlite3.connect(".\doctor\drDetailsFile.db")
    doctorCursor=connect.cursor()

    def createTable():
        # Create table
            create_table='''
                CREATE TABLE ptDetailsTable (
                    Name TEXT,
                    Age INT ,
                    Gender TEXT,
                    Emergency TEXT
                    )
                    '''
            patientCursor.execute(create_table)
    # createTable()

    def insertTable():
        #insert
            name=input("Enter Name: ")
            age=input("Enter Age: ")
            gender=input("Enter gender: ")
            emergency=input("Is it emergency(yes/no)? ")

            insert_script=f'''INSERT INTO ptDetailsTable VALUES (
                    "{name}",
                    "{age}",
                    "{gender}",
                    "{emergency}"
                    )'''
            patientCursor.execute(insert_script)
            conn.commit()
    # insertTable()

    def searchTable():
        # Read Data
            select_cmd= '''SELECT * FROM ptDetailsTable'''
            result=patientCursor.execute(select_cmd)
            print("*"*20)
            print("YOUR RECORD")
            for data in result:        
                print(f"Name: {data[0]}")
                print(f"Age: {data[1]}")
                print(f"Gender: {data[2]}")
                print(f"Emergency: {data[3]}")
            conn.commit        
    

    press=int(input("Press 2 to view details and 3 to log in new record: "))
    if press==2:
                    searchTable()

    if press==3:
                    insertTable()
                    searchTable()
   
                
    def searchDoctors():
                select_cmd='''SELECT  * FROM drDetailsTable'''
                result=doctorCursor.execute(select_cmd)
                count=0
                for data in result:
                    if(data[4].lower()=="yes"):
                        count+=1
                        if(count==1):
                            print('The name of available doctors are:\n')
                        print(f"Name:{data[0]}") 
                        print(f"Contact: {data[1]}")
                        print(f"Availability: {data[4]}")
                return count



    choice=input('Do you want to check if doctors are available? type yes/no: ')
    try:
        if(choice.lower()=="yes"):                
                if(searchDoctors()==0):
                        print('Sorry,no doctors are available at the moment')
    except:
        print("No doctors available at the moment.")
        x=input("Confirm emergency? ")
        if(x.lower()=="yes"):
            print("Please refer to hotline number refered below: \n 1618-01-4288919")
                        
        
                
    


