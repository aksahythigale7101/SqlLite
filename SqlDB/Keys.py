
import sqlite3

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
        print()
        cursor.execute(f"SELECT * FROM {TableName}")
        # cursor.execute("DELETE FROM EMPLOYEE WHERE EmployeeId = ?",(106,))
        compnayDB.conn.commit()
        rows = cursor.fetchall()
        # for row in rows:
        #   print(row ,"--")
        Headers = ["DepartmentId ", "DepartmentName"]
        Headers1 = ["EmployeeId ", "Name", "Age", "Salary", "City", "DepartmentId"]

        print(f"-------------------{TableName}----------------")
        print(
            "\n"
            + tabulate(
                rows,
                headers=Headers if TableName == "DEPARTMENT" else Headers1,
                tablefmt="grid",
            )
        )

    def Drop_Table(TableName):
        cursor.execute(f"DROP TABLE IF EXISTS {TableName}")
        compnayDB.conn.commit()
        print("Employee table dropped successfully!")

    def InsertEmp(EmpId, EName, age, salary, city, DeptID):
        try:

            cursor.execute(
                "INSERT INTO EMPLOYEE(EmployeeId,Name,Age,Salary,City,DepartmentId) VALUES (?,?,?,?,?,?)",
                (EmpId, EName,age,salary,city, DeptID),
            )
            compnayDB.conn.commit()
            print("Insert Data Succesfully")
        except Exception as e:
            print(f"Error Name : {type(e).__name__}")
            print(f"Error Details: {e}")

    def delete_row(TableName, ColumeName, ID):
        # cursor.execute("DELETE FROM EMPLOYEE WHERE EmployeeId = ?",(106,))
        try:
            cursor.execute(f"DELETE FROM {TableName} WHERE {ColumeName} = ?", (ID,))
            compnayDB.conn.commit()
        except Exception as e:
            print(f"Error Name : {type(e).__name__}")
            print(f"Error Details: {e}")

    def update_row(TableName, ColumeName, ID):
        try:
            cursor.execute(
                f"UPDATE {TableName} SET DepartmentId={ColumeName} WHERE DepartmentId={ID}"
            )
            compnayDB.conn.commit()
        except Exception as e:
            print(f"Error Name : {type(e).__name__}")
            print(f"Error Details: {e}")
