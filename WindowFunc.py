from tabulate import tabulate

from Connection import _Db1 as CompanyDB

cursor_comp = CompanyDB.conn.cursor()

import sqlite3


class WinFunction:
    def NoramlAggregate():
        query = "SELECT Name, SUM(Salary) FROM EMPLOYEE" " GROUP BY DepartmentId"

        WinFunction.ReadData(query, "", "Aggregat Function")

    def Over_Partion():
        query = (
            "SELECT *,"
            " SUM(Salary)"
            " OVER (PARTITION  BY DepartmentId) as DeptTotal "
            " FROM EMPLOYEE"
        )
        # print(sqlite3.sqlite_version)
        WinFunction.ReadData(query, "", "Over/Partion Total")

    def ROW_NUMBER():
        query1 = (
            "SELECT *,"
            "  ROW_NUMBER()"
            " OVER (PARTITION  BY DepartmentId) as DeptTotal "
            " FROM EMPLOYEE"
        )
        query2 = (
        "SELECT * FROM ("
        "  SELECT *, "
        "  ROW_NUMBER() OVER (PARTITION BY DepartmentId ORDER BY City DESC) AS rn "
        "  FROM EMPLOYEE"
        ") t "
        "WHERE rn = 1"
    )

        # print(sqlite3.sqlite_version)
        WinFunction.ReadData(query2, "", "Row_Number")

    @staticmethod
    def ReadData(Query, parms, comment):
        print(f"-------------{comment}---------------")
        cursor_comp.execute(Query, parms)
        # Keys.compnayDB.conn.commit()
        rows = cursor_comp.fetchall()
        Headers1 = [
            "EmployeeId ",
            "Name",
            "Age",
            "Salary",
            "City",
            "DepartmentId",
            f"{comment}",
        ]
        print(
            "\n"
            + tabulate(
                rows,
                headers=Headers1,
                tablefmt="grid",
            )
        )