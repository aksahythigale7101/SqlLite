import sqlite3
# 1. Import the active database instance
from Connection import _Db as DB



# from connectionDb    import    _Db
#        ↑                         ↑
#      File/Module              Variable/Instance




class CREATE_TABLE:

    @staticmethod
    def MakeTable():
        # 2. FIX: Create the cursor INSIDE the function using the imported Dba instance
        cursor = DB.conn.cursor()

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



# 4. Actually execute the function
#CREATE_TABLE.MakeTable()

class InsertData:
  
    def InsertData(self,name, age, email, course):
        cursor = DB.conn.cursor()
        cursor.execute(
            "INSERT INTO STUDENTS (name, age, email, course) VALUES (?, ?, ?, ?)",
            (name, age, email, course)
        )
        DB.conn.commit()
        print(f"Inserted data for {name} successfully!")


Is=InsertData()
Is.InsertData ('Rahul Sharma', 21, 'rahul@example.com', 'Computer Science');

Is.InsertData('Priya Deshmukh', 22, 'priya.d@example.com', 'Data Science');
Is.InsertData('Aman Verma', 20, 'aman.verma@example.com', 'Computer Science');
Is.InsertData('Sneha Kulkarni', 23, 'sneha.k@example.com', 'Information Technology');
Is.InsertData('Rohan Patil', 21, 'rohan.patil@example.com', 'Electronics');
Is.InsertData('Ananya Joshi', 22, 'ananya.j@example.com', 'Computer Science');

#Is.InsertData('jow', 22, 'Jo.j@example.com', 'Computer Science');

