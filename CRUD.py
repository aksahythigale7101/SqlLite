import sqlite3

from tabulate import tabulate
from Connection import _Db as DB

class CRUD_Operation:
     @staticmethod
     def ReadData():
        cursor = DB.conn.cursor()
        cursor.execute("SELECT * FROM STUDENTS")
        rows = cursor.fetchall()
        # for row in rows:
        #     print(row)

        Headers=["ID","Name", "Age", "Email", "Course","Date"]
        print("\n" + tabulate(rows, headers=Headers, tablefmt="grid"))

     @staticmethod
     def InsertData(name, age, email, course):

         #ursor.execute("INSERT INTO DEPARTMENT(EmployeeId, DepartmentName) VALUES (%s, %s)", (Eid, DeprtName)) USED IN MYSQL

        cursor = DB.conn.cursor()

        cursor.execute(
            "INSERT INTO STUDENTS (name, age, email, course) VALUES (?, ?, ?, ?)",  #THIS IS TYPE USED SQLlITE
            (name, age, email, course)
        )
        DB.conn.commit()
        print(f"Inserted data for {name} successfully!")
            
     @staticmethod
     def UpdateData(student_id, name):
        cursor = DB.conn.cursor()
        query="UPDATE STUDENTS SET Name= ? Where id= ?"
        values=(student_id,name) # always first paramter is where paremter and second is value to be updated
        cursor.execute(query,values)
        DB.conn.commit()
        print("Update Data Succesfully",student_id)
     
     @staticmethod  
     def DeleteData(student_id):
        cursor = DB.conn.cursor()
        query="DELETE FROM STUDENTS WHERE id= ?"
        values=(student_id,) # always first paramter is where paremter and second is value to be updated
        cursor.execute(query,values)
        DB.conn.commit()
        print("Delete Data Succesfully",student_id)
        
            