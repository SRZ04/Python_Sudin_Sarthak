def doctorCredentialsFunction():
    import sqlite3
    conn=sqlite3.connect(".\doctor\drCredentialsFile.db")
    doctorCursor=conn.cursor()

    def createTable():
    # Create table
        create_table='''
            CREATE TABLE drCredentialsTable (
                username TEXT PRIMARY KEY,
                password TEXT)
                '''
        doctorCursor.execute(create_table)
    # createTable()

    def insertTable():
    #insert
        loginUsername=input("Enter username: ")
        loginPassword=input("Enter password: ")
        insert_script=f'''INSERT INTO drCredentialsTable VALUES (
                "{loginUsername}",
                "{loginPassword}")'''
        doctorCursor.execute(insert_script)
        conn.commit()


    def searchTable():
    # Read Data
        select_cmd= '''SELECT * FROM drCredentialsTable'''
        result=doctorCursor.execute(select_cmd)
        print("*"*20)
        count=0
        for data in result:        
            # print(f"username: {data[0]}")
            # print(f"password: {data[1]}")
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
        doctorCursor.close()

    #LOGIN WINDOW
    print("*"*20)
    print("WELCOME TO DOCTOR LOGIN WINDOW")
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


