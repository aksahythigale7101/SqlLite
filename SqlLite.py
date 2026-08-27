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



from Keys import keys

'''
Iquery=(1,"IT")
Iquery=(2,"HR")
Iquery=(3,"Finance")
Iquery=(4,"Sales")
if keys.InsertDepat(Iquery):
   print(f"Data Insert Succesfully {Iquery[1]}")
else:
   print("Data Is not Inserted")
'''


# keys.Drop_Table("Employee")

keys.ReadData("DEPARTMENT") # Department Table is the Parent because its DepartmentId is referenced.

'''
keys.InsertEmp(101, "Akshay", 1)
keys.InsertEmp(102, "Rahul", 2)
keys.InsertEmp(103, "Amit", 1)#Duplicate accpect
keys.InsertEmp(104, "Sneha", 3)
keys.InsertEmp(105, "Abhay", 4)
keys.InsertEmp(106, "Ranjeet",  None)# null is accpect until when we cerate table coulmn set as not null
keys.InsertEmp(106, "Harsh", 99) # no added becuase is not present DeptID 9 in Deparetment table DepetID  cause of forgien key
'''

# keys.delete_row("DEPARTMENT","DepartmentId",1)# not delete beacuse the Id 1 refreance presetn in employee table
#keys.delete_row("EMPLOYEE","DepartmentId",1)# not delete beacuse the Id 1 refreance presetn in employee table

# keys.update_row("DEPARTMENT",10,1)

keys.ReadData("EMPLOYEE") #Employee Table is the Child because it contains the Foreign Key.



#keys.delete_row("DEPARTMENT","DepartmentId",1) using ON DELETE CASCADE parent recorde delete as well as child recode delete


#keys.update_row("DEPARTMENT",10,1) usind ON UPDATE CASCADE parent recode update as well ad childe recode update both table replace 1 and put 10

# ON DELTE SET NULL CASCADE IS Used when parent recode is delete but child recode is not delete where refrance recode in chile the
                     # table put the null value