import sqlite3
import stat
# 1. Import the active database instance
from Connection import _Db as DB
from Connection import _Db1 as compnayDB


# from connectionDb    import    _Db
#        ↑                         ↑
#      File/Module              Variable/Instance




class CREATE_TABLE:

    @staticmethod
    def MakeTable():
        # 2. FIX: Create the cursor INSIDE the function using the imported Dba instance
        cursor = DB.conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='STUDENTS'")
        table_exists=cursor.fetchone()
        # if table_exists :
        #      print("Table Is alredy created")
        #      return
        if checkTableExist(table_exists):
            return



        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS STUDENTS
            (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             age INTEGER NOT NULL,
             email TEXT UNIQUE NOT NULL,
             course TEXT,
             enrollment_date TEXT DEFAULT (date('now'))
            )
            """
        )

        # 3. FIX: Commit the changes back to the database using Dba
        DB.conn.commit()
        print("Table accounts created successfully!")
    



class CREATE_COMPANY_TABLE:
   
    @staticmethod
    def DepartmentTable():
         cursor = compnayDB.conn.cursor()
         
         cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='DEPARTMENT'")
         table_exists=cursor.fetchone()
         # if table_exists :
         #     print("Table Is alredy created")
         #     return
         if checkTableExist(table_exists):
            return

         cursor.execute("""
           CREATE TABLE IF NOT EXISTS DEPARTMENT(
           DepartmentId  INTEGER PRIMARY KEY,
           DepartmentName TEXT
            )"""
         )
         compnayDB.conn.commit()
         print ("Department Table Create Successfully !")
         
    def EmployeeTable():
        cursor = compnayDB.conn.cursor()

        compnayDB.conn.execute("PRAGMA foreign_keys = ON;")#प्रॉब्लेम असा आहे की SQLite मध्ये FOREIGN KEY फक्त टेबलमध्ये लिहिल्याने आपोआप enforce होत नाही.
                                                            #प्रत्येक वेळी connection उघडल्यावर तुला वेगळी command देऊन ते ON करावं लागतं:


        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Employee'")
        table_exists=cursor.fetchone()
        if checkTableExist(table_exists):
           return
        
        cursor.execute("""
          CREATE TABLE IF NOT EXISTS Employee(
          EmployeeId INTEGER PRIMARY KEY,
          Name TEXT,
          DepartmentId INTEGER,

          FOREIGN KEY (DepartmentId)
            REFERENCES Department(DepartmentId)

          )"""
        )
        compnayDB.conn.commit()
        print ("Employee Table Create Successfully !")
        







def checkTableExist(table_exists):
      if table_exists :
             #print("Table Is alredy created")
             return True


# 4. Actually execute the function
CREATE_TABLE.MakeTable()

CREATE_COMPANY_TABLE.DepartmentTable()


CREATE_COMPANY_TABLE.EmployeeTable()    

   





