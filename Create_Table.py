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
CREATE_TABLE.MakeTable()



