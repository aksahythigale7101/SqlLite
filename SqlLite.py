#   python -c "import sqlite3;
#   print(sqlite3.sqlite_version)" // showing on console
# this commond is used to check the version of sqlite3 installed in your python environment.

import Connection

import Create_Table
from CRUD import CRUD_Operation  #option 2 -----import CRUD
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

"""
# CRUD_Operation.ReadData()


from Keys import keys

'''
Iquery=(1,"IT")
Iquery=(2,"HR")
Iquery=(3,"Finance")
Iquery=(4,"Sales")
Iquery=(5,"Marketing")
if keys.InsertDepat(Iquery):
   print(f"Data Insert Succesfully {Iquery[1]}")
else:
   print("Data Is not Inserted")
'''


#keys.Drop_Table("Employee")

keys.ReadData("DEPARTMENT") # Department Table is the Parent because its DepartmentId is referenced.

''' #old table 
keys.InsertEmp(101, "Akshay", 1)
'''
#keys.InsertEmp(106, "Harsh", 99) # no added becuase is not present DeptID 9 in Deparetment table DepetID  cause of forgien key

'''
keys.InsertEmp(101, 'Akshay', 30, 55000, 'Pune', 1)
keys.InsertEmp(102, 'Rahul', 28, 60000, 'Mumbai', 1)#Duplicate accpect allow
keys.InsertEmp(103, 'Amit', 35, 45000, 'Pune', 2)
keys.InsertEmp(104, 'Sneha', 27, 50000, 'Mumbai', 2)#Duplicate accpect allow
keys.InsertEmp(105, 'Vijay', 32, 75000, 'Pune', 3)
keys.InsertEmp(106, 'Priya', 29, 65000, 'Delhi', 3)
keys.InsertEmp(107, 'Rohit', 26, 40000, 'Pune', 4)
keys.InsertEmp(108, 'Neha', 31, 70000, 'Mumbai', 5)
keys.InsertEmp(109, 'Kiran', 34, 80000, 'Delhi', 5)
keys.InsertEmp(110, 'Pooja', 25, 35000, 'Pune', 4)
keys.InsertEmp(111, "Ranjeet",25,32500,'Pune', None)# null is accpect until when we cerate table coulmn set as not null
'''







# keys.delete_row("DEPARTMENT","DepartmentId",1)# not delete beacuse the Id 1 refreance presetn in employee table
#keys.delete_row("EMPLOYEE","DepartmentId",1)# not delete beacuse the Id 1 refreance presetn in employee table

# keys.update_row("DEPARTMENT",10,1)

keys.ReadData("EMPLOYEE") #Employee Table is the Child because it contains the Foreign Key.



#keys.delete_row("DEPARTMENT","DepartmentId",1) using ON DELETE CASCADE parent recorde delete as well as child recode delete


#keys.update_row("DEPARTMENT",10,1) usind ON UPDATE CASCADE parent recode update as well ad childe recode update both table replace 1 and put 10

# ON DELTE SET NULL CASCADE IS Used when parent recode is delete but child recode is not delete where refrance recode in chile the
                     # table put the null value




#------------------------------------------------------------------------
#"-------------------Join Output-------------------------"
'''
from Join import _join 

_join.innerJoin()
_join.LeftJoin()
_join.RightJoin()
'''

#------------------------------------Group with having----------------------

from Claues import claues

claues.Groupby()
claues.where()