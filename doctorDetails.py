def doctorDetailsFuntion():
    from doctorCredentials import doctorCredentialsFunction
    
    import sqlite3
    conn=sqlite3.connect(".\doctor\drDetailsFile.db")
    doctorCursor=conn.cursor()

    ptconn=sqlite3.connect(".\doctor\ptDetailsFile.db")
    patientCursor=ptconn.cursor()

            
    # def searchCredentialsTable():
    #     # Read Data
    #         select_cmd= '''SELECT * FROM drCredentialsTable'''
    #         result=doctorCursor.execute(select_cmd)
    #         for data in result: 
    #             return data[0]

    def createTable():
    # Create table
        create_table='''
            CREATE TABLE drDetailsTable (
                Name TEXT,
                Contact TEXT PRIMARY KEY,
                Degree TEXT,
                Experience_Years INT,
                Available TEXT
                )
                '''
        doctorCursor.execute(create_table)
    createTable()

    def insertTable():
    #insert
        name=input("Enter Name: ")
        contact=input("Enter Contact: ")
        degree=input("Enter Degree: ")
        expYear=input("Enter Experience Year: ")
        available=input("Are you available(yes/no)? ")

        insert_script=f'''INSERT INTO drDetailsTable VALUES (
                "{name}",
                "{contact}",
                "{degree}",
                "{expYear}",
                "{available}")'''
        doctorCursor.execute(insert_script)
        conn.commit()


    def searchTable():
    # Read Data
        select_cmd= '''SELECT * FROM drDetailsTable'''
        result=doctorCursor.execute(select_cmd)
        print("*"*20)
        print("YOUR RECORD")
        for data in result:     
            print("_"*20)   
            print(f"Name: {data[0]}")
            print(f"Contact: {data[1]}")
            print(f"Degree: {data[2]}")
            print(f"Experience year: {data[3]}")
            print(f"Availability: {data[4]}")

        conn.commit
        doctorCursor.close()

    # def searchDrAvailableTable():
    # # Return Availability
    #     select_cmd= '''SELECT * FROM drDetailsTable'''
    #     result=doctorCursor.execute(select_cmd)
    #     print("*"*20)
    #     print("YOUR RECORD")
    #     for data in result: 
    #         return {data[4]}


    press=int(input("Press 2 to view details and 3 to log in new record: "))

    if press==2:
        searchTable()

    if press==3:
        insertTable()
        searchTable()
    
    
    def searchPatientTable():
        # Read Data
        select_cmd= '''SELECT * FROM ptDetailsTable'''
        result=patientCursor.execute(select_cmd)
        print("*"*20)
        print("PATIENT RECORD")
        for data in result:        
            print(f"Name: {data[0]}")
            print(f"Age: {data[1]}")
            print(f"Gender: {data[2]}")
            print(f"Emergency: {data[3]}")
        conn.commit

    check=input("Type yes to check patient details: ")
    if check.lower()=="yes":
        searchPatientTable()