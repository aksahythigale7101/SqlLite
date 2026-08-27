from calendar import c
import sqlite3
from token import COMMA
from Connection import _Db1 as compnayDB

from tabulate import tabulate

cursor = compnayDB.conn.cursor()


class keys:
    def InsertDepat(_iquery):
        try:
            Eid = _iquery[0]
            DeprtName = _iquery[1]

            # cursor=compnayDB.conn.cursor()
            cursor.execute(
                "INSERT INTO DEPARTMENT(DepartmentId,DepartmentName) VALUES (?,?) ",
                (Eid, DeprtName),
            )
            compnayDB.conn.commit()

            return True
        except Exception as e:
            compnayDB.conn.rollback()
            print(f"-- {e}")
            return False

    def ReadData(TableName):
        
        cursor.execute(f"SELECT * FROM {TableName}")
        #cursor.execute("DELETE FROM EMPLOYEE WHERE EmployeeId = ?",(106,))
        compnayDB.conn.commit()
        rows = cursor.fetchall()
        # for row in rows:
        #   print(row ,"--")
        Headers = ["DepartmentId ", "DepartmentName"]
        Headers1 = ["EmployeeId ", "Name", "DepartmentId"]

     

        
        print(f"-------------{TableName}-------------")
        print(
            "\n"
            + tabulate(
                rows,
                headers=Headers if TableName == "DEPARTMENT" else Headers1,
                tablefmt="grid",
            )
        )

    def Drop_Table():
        cursor.execute("DROP TABLE IF EXISTS Employee")
        compnayDB.conn.commit()
        print("Employee table dropped successfully!")

    def InsertEmp(EmpId, EName, DeptID):
        try:

            cursor.execute(
                "INSERT INTO EMPLOYEE(EmployeeId,Name,DepartmentId) VALUES (?,?,?)",
                (EmpId, EName, DeptID),
            )
            compnayDB.conn.commit()
            print("Insert Data Succesfully")
        except Exception as e:
            print(f"Error Name : {type(e).__name__}")
            print(f"Error Details: {e}")
    


    def delete_row(TableName,ColumeName,ID):
      #cursor.execute("DELETE FROM EMPLOYEE WHERE EmployeeId = ?",(106,))
      try:
         cursor.execute(f"DELETE FROM {TableName} WHERE {ColumeName} = ?",(ID,))
         compnayDB.conn.commit()
      except Exception as e:
            print(f"Error Name : {type(e).__name__}")
            print(f"Error Details: {e}")





