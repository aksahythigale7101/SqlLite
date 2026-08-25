#   python -c "import sqlite3; print(sqlite3.sqlite_version)"
#this commond is used to check the version of sqlite3 installed in your python environment.

import Connection

#import Create_Table
#import CRUD

from CRUD import CRUD_Operation

CRUD_Operation.InsertData('jow', 22, 'Jo.j@example.com', 'Computer Science');
#CRUD_Operation.UpdateData("Pooja Kharde",2)
#CRUD_Operation.DeleteData(10)
CRUD_Operation.ReadData()



# Is.InsertData ('Rahul Sharma', 21, 'rahul@example.com', 'Computer Science');

# Is.InsertData('Priya Deshmukh', 22, 'priya.d@example.com', 'Data Science');
# Is.InsertData('Aman Verma', 20, 'aman.verma@example.com', 'Computer Science');
# Is.InsertData('Sneha Kulkarni', 23, 'sneha.k@example.com', 'Information Technology');
# Is.InsertData('Rohan Patil', 21, 'rohan.patil@example.com', 'Electronics');
# Is.InsertData('Ananya Joshi', 22, 'ananya.j@example.com', 'Computer Science');
