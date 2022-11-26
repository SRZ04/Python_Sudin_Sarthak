def patientCredentialsFunction():
    import sqlite3
    conn=sqlite3.connect(".\doctor\ptCredentialsFile.db")
    patientCursor=conn.cursor()

    def createTable():
    # Create table
        create_table='''
            CREATE TABLE ptCredentialsTable (
                username TEXT PRIMARY KEY,
                password TEXT)
                '''
        patientCursor.execute(create_table)
    # createTable()

    def insertTable():
    #insert
        loginUsername=input("Enter username: ")
        loginPassword=input("Enter password: ")
        insert_script=f'''INSERT INTO ptCredentialsTable VALUES (
                "{loginUsername}",
                "{loginPassword}")'''
        patientCursor.execute(insert_script)
        conn.commit()


    def searchTable():
    # Read Data
        select_cmd= '''SELECT * FROM ptCredentialsTable'''
        result=patientCursor.execute(select_cmd)
        print("*"*20)
        count=0
        for data in result:        
            if loginUsername==(f"{data[0]}") and loginPassword==(f"{data[1]}"):
                count+=1 
        if count==1:
            print("*"*20)
            print("Login Successful") 
            print("*"*20)
        else:
            print("*"*20)
            print("Login Failed")    
            print("*"*20)      
        conn.commit
        patientCursor.close()

    #LOGIN WINDOW
    print("*"*20)
    print("WELCOME TO PATIENT LOGIN WINDOW")
    print("*"*20)
    login=int(input("Press 0 to login and 1 to register: "))

    if login==1:
        loginUsername=input("Enter username: ")
        loginPassword=input("Enter password: ")
        print("*"*20)
        print("Registration Successful")
        print("*"*20)
        insertTable()
        searchTable()       

    if login==0:
        loginUsername=input("Enter username: ")
        loginPassword=input("Enter password: ")
        searchTable()


