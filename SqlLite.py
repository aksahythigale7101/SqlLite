#   python -c "import sqlite3; print(sqlite3.sqlite_version)"
#this commond is used to check the version of sqlite3 installed in your python environment.

import Connection

#import Create_Table
#import CRUD

from CRUD import CRUD_Operation


#CRUD_Operation.UpdateData("Pooja Kharde",2)
#CRUD_Operation.DeleteData(7)
CRUD_Operation.ReadData()