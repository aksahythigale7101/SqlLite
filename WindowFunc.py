from tabulate import tabulate

from Connection import _Db1 as CompanyDB

cursor_comp = CompanyDB.conn.cursor()


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
            "SELECT *, "
            "  ROW_NUMBER()"
            " OVER (PARTITION  BY DepartmentId) as DeptTotal "
            " FROM EMPLOYEE"
        )
        '''
        query2 = (
        "SELECT * FROM ("#EMPLOYEE टेबलमधले सगळे रेकॉर्ड्स घेतले जातात.
        "  SELECT *, "
        "  ROW_NUMBER() "#ROW_NUMBER() म्हणजे — प्रत्येक गटात प्रत्येक रेकॉर्डला एक क्रमांक (1, 2, 3...) दिला जातो.
                         # सगळ्यात जास्त पगार असलेल्याला 1 नंबर मिळतो, त्याखालच्याला 2, वगैरे.
        "OVER (PARTITION BY DepartmentId " #PARTITION BY DepartmentId म्हणजे — सगळ्या employees ना त्यांच्या 
                                                                     # DepartmentId नुसार वेगवेगळ्या गटांत (groups) विभागायचं.
        
        "ORDER BY salary DESC) "#ORDER BY salary DESC म्हणजे — प्रत्येक गटाच्या आत employees ना पगारानुसार #(जास्त ते कमी) क्रमवारी लावायची. 
                                                                                        
         "AS rn "   #हा क्रमांक rn नावाच्या नवीन कॉलममध्ये साठवला जातो.
        "  FROM EMPLOYEE"
        ") t " #इथे t हे फक्त एक alias (टोपणनाव) आहे
        "WHERE rn = 1" #वरच्या रिझल्टमधून फक्त तेच रेकॉर्ड्स निवडले जातात ज्यांचा rn = 1 आहे.
    )
    '''
        query2 = (
            "SELECT * FROM("
            "SELECT *, "
            "  ROW_NUMBER()"
            " OVER (PARTITION  BY DepartmentId ORDER BY SALARY DESC) as rn "
            " FROM EMPLOYEE"
            ")t "
            "WHERE rn = 1"
        )

        # print(sqlite3.sqlite_version)
        WinFunction.ReadData(query1, "", "Row_Number")

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
