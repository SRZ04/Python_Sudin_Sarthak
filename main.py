import sqlite3
conn=sqlite3.connect(".\doctor\drDetailsFile.db")
mycursor=doctorCursor=conn.cursor()

connect=sqlite3.connect(".\doctor\ptCredentialsFile.db")
patientCursor=connect.cursor()

from patientCredentials import patientCredentialsFunction
from patientDetails import patientDetailsFunction

from doctorCredentials import doctorCredentialsFunction
from doctorDetails import doctorDetailsFuntion

from admin import Admin

adminObj=Admin

check=input("Enter doctor or patient or admin: ")
if check.lower()=="patient":
    patientCredentialsFunction()
    patientDetailsFunction()

if check.lower()=="doctor":
    doctorCredentialsFunction()
    doctorDetailsFuntion()

if check.lower()=="admin":
    adminObj.Check()




