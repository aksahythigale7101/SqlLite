#   python -c "import sqlite3;
#   print(sqlite3.sqlite_version)" // showing on console
# this commond is used to check the version of sqlite3 installed in your python environment.

import Connection

import Create_Table

"""
from CRUD import CRUD_Operation  #option 2 -----import CRUD

#CRUD_Operation.InsertData('jow', 22, 'Jo.j@example.com', 'Computer Science');
# Is.InsertData ('Rahul Sharma', 21, 'rahul@example.com', 'Computer Science');
# Is.InsertData('Priya Deshmukh', 22, 'priya.d@example.com', 'Data Science');
# Is.InsertData('Aman Verma', 20, 'aman.verma@example.com', 'Computer Science');
# Is.InsertData('Sneha Kulkarni', 23, 'sneha.k@example.com', 'Information Technology');
# Is.InsertData('Rohan Patil', 21, 'rohan.patil@example.com', 'Electronics');
# Is.InsertData('Ananya Joshi', 22, 'ananya.j@example.com', 'Computer Science');


#CRUD_Operation.UpdateData("Pooja Kharde",2)
#CRUD_Operation.DeleteData(10)
CRUD_Operation.ReadData()
"""

# import Keys

from Keys import keys

"""
#Iquery=(1,"IT")
#Iquery=(2,"HR")
#Iquery=(3,"Finance")
Iquery=(4,"Sales")
if keys.InsertDepat(Iquery):
   print(f"Data Insert Succesfully {Iquery[1]}")
else:
   print("Data Is not Inserted")
"""
# keys.Drop_Table()
keys.ReadData("DEPARTMENT")

#keys.InsertEmp(101, "Akshay", 1)
#keys.InsertEmp(102, "Rahul", 2)
#keys.InsertEmp(103, "Amit", 1)
#keys.InsertEmp(104, "Sneha", 3)

keys.ReadData("EMPLOYEE")