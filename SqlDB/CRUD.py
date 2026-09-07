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

        Headers = ["ID", "Name", "Age", "Email", "Course", "Date"]
        print("\n" + tabulate(rows, headers=Headers, tablefmt="grid"))

    @staticmethod
    def InsertData(name, age, email, course):

        # ursor.execute("INSERT INTO DEPARTMENT(EmployeeId, DepartmentName) VALUES (%s, %s)", (Eid, DeprtName)) USED IN MYSQL

        cursor = DB.conn.cursor()

        cursor.execute(
            "INSERT INTO STUDENTS (name, age, email, course) VALUES (?, ?, ?, ?)",  # THIS IS TYPE USED SQLlITE
            (name, age, email, course),
        )
        DB.conn.commit()
        print(f"Inserted data for {name} successfully!")

    @staticmethod
    def UpdateData(age, student_id):
        cursor = DB.conn.cursor()
        query = "UPDATE STUDENTS SET age= ? Where id= ?"
        values = (age, student_id)
        cursor.execute(query, values)
        DB.conn.commit()
        print("Update Data Succesfully", student_id)

    def ChekTableColum():
        cursor = DB.conn.cursor()
        cursor.execute("PRAGMA table_info(STUDENTS)")
        #columns = cursor.fetchall()
        #for column in columns:
         #   print(column)

        #cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='STUDENTS'")
        #print(cursor.fetchone())
        

        cursor.execute("PRAGMA database_list")
        print(cursor.fetchall())

    @staticmethod
    def DeleteData(student_id):
        cursor = DB.conn.cursor()
        query = "DELETE FROM STUDENTS WHERE id= ?"
        values = (
            student_id,
        )  # always first paramter is where paremter and second is value to be updated
        cursor.execute(query, values)
        DB.conn.commit()
        print("Delete Data Succesfully", student_id)

    def Drop_Table():
        cursor = DB.conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS STUDENTS")
        DB.conn.commit()
        print("Employee table dropped successfully!")