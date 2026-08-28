from Connection import _Db as studentDB
from Connection import _Db1 as CompanyDB


cursor_stud = studentDB.conn.cursor()
cursor_comp = CompanyDB.conn.cursor()


class claues:
    def Groupby():
        query = "SELECT Course, COUNT(ID) FROM STUDENTS " "GROUP BY Course"

        query1 = (
            "SELECT  D.DepartmentName ,COUNT(*)  FROM EMPLOYEE E INNER JOIN DEPARTMENT D "
            "ON E.DepartmentId=D.DepartmentId "
            "GROUP BY DepartmentName "
            "ORDER  BY E.NAME ASC"
        )

        query2 = (
            "SELECT Count(E.salary), MAX(E.salary),D.DepartmentName FROM EMPLOYEE E INNER JOIN DEPARTMENT D "
            "ON E.DepartmentId=D.DepartmentId "
            "GROUP BY D.DepartmentName "
        )

        query3 = (
            "SELECT  D.DepartmentName ,COUNT(*) AS EmployeeCount  FROM EMPLOYEE E INNER JOIN DEPARTMENT D "
            "ON E.DepartmentId=D.DepartmentId "
            "GROUP BY D.DepartmentName "
            "HAVING COUNT(*) > 1"
        )

        query4 = (
            "SELECT  D.DepartmentName,E.Name ,E.City   FROM EMPLOYEE E INNER JOIN DEPARTMENT D "
            "ON E.DepartmentId=D.DepartmentId "
           
            "WHERE E.City=('Delhi') "
        )

        claues.ReadData(
            cursor_comp, query4, "", "GROUP BY"
        )  # change as per datbase cursor

    def where():
        query = "SELECT * FROM STUDENTS WHERE COURSE = ?"
        values = ("Computer Science",)

        query1 = "SELECT * FROM EMPLOYEE WHERE Name  LIKE  ('A%')"
        values1 = ("")
        claues.ReadData(cursor_comp, query1, values1, "WHERE")

    @staticmethod
    def ReadData(database, Query, parms, comment):
        print(f"-------------{comment}---------------")
        database.execute(Query,parms)
        rows = database.fetchall()
        for row in rows:
            print(row)
