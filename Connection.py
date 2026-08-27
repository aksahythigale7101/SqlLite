

import sqlite3


class ConnectionDatabase:

    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)

            #print("Database connected successfully.")
        except sqlite3.Error as e:
            self.conn = None
            #print(f"Database connection failed: {e}")


# Create the single instance HERE so other files can import it
_Db = ConnectionDatabase("Collage.db")

_Db1 =ConnectionDatabase("Compnay.db")
               






    
        
       