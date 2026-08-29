from Connection import _Db as studentDB
from Connection import _Db1 as CompanyDB
import Keys


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
            cursor_comp, query2, "", "GROUP BY"
        )  # change as per datbase cursor

    def where():
        query = "SELECT * FROM STUDENTS WHERE COURSE = ?"
        values = ("Computer Science",)

        query1 = (
            "SELECT * FROM EMPLOYEE "
            # "WHERE Name  LIKE  ('R%')")
            "WHERE DepartmentId IS NULL"
        )
        values1 = ""

        query2 = (
            "SELECT * ,MAX(SALARY) FROM EMPLOYEE "
            "WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE )"
        )  # select higest second salary

        query3 = (
            "SELECT City ,COUNT(*) FROM EMPLOYEE " "GROUP BY City"
        )  # no of emp located in city with count

        query4 = (
            "SELECT CITY,COUNT(*) FROM EMPLOYEE "
            "GROUP BY CITY "
            "HAVING COUNT(CITY) > 3"
        )  # no of emp wich are located more then 3 in same area

        query5 = (
            "SELECT *,MAX(SALARY)  FROM EMPLOYEE "  # City wise higest salary from emloyee
            "GROUP BY CITY"
        )
        query6 = (
            "SELECT Name  FROM Employee WHERE DepartmentId = (SELECT DepartmentId FROM Department "
            "WHERE DepartmentName = 'IT')"
        )

        query7 = (
            "SELECT NAME ,SALARY FROM EMPLOYEE "
            "WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE)"  # total avergae above greater then salary empmpoye
        )

        claues.ReadData(cursor_comp, query7, values1, "WHERE")

    def Union():
        query1 = (
            "SELECT EmployeeId , Name FROM EMPLOYEE "
            "WHERE CITY= 'Pune' "
            "UNION "  # "UNION ALL "
            "SELECT EmployeeId,Name FROM Employee "
            # "WHERE City = 'Mumbai' "
            "WHERE City = 'Pune' "
        )

        claues.ReadData(cursor_comp, query1, "", "UNION  OR UNION ALL")

    def case():
        query1 = (
            "SELECT NAME,AGE,SALARY, "
            "CASE "
            # "WHEN AGE>=30 THEN 'Too age 30 is crossed '"
            "WHEN SALARY>=70000 THEN 'High' "
            "WHEN SALARY>=40000 THEN 'Meduim' "
            "ELSE 'LOW '"
            "END  "
            "FROM EMPLOYEE "
        )

        claues.ReadData(cursor_comp, query1, "", "CASE")

    def CTE():
        query1 = (
            "WITH SecondHighestSalary AS "
            "(SELECT Name,MAX(SALARY) FROM EMPLOYEE "
            "WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE)) "
            "SELECT Name FROM SecondHighestSalary"
        )
        query2 = (
            "WITH AveragSalary As"
            " (SELECT NAME ,SALARY FROM EMPLOYEE"
            " WHERE SALARY > (SELECT AVG(SALARY)FROM EMPLOYEE))"
            " SELECT NAME ,SALARY  FROM AveragSalary"
        )

        claues.ReadData(cursor_comp, query2, "", "CTE")

    def view():
        cursor_comp.execute(
            "CREATE VIEW IF NOT EXISTS InnerJoin As"
            " SELECT EmployeeId, Name,Salary,City,DepartmentName FROM EMPLOYEE INNER JOIN DEPARTMENT"
            " ON EMPLOYEE.DepartmentId = DEPARTMENT.DepartmentId"
        )

        Query1 = "SELECT * FROM InnerJoin"

        cursor_comp.execute(
            "CREATE VIEW IF NOT EXISTS CityArea As "
            "SELECT * FROM EMPLOYEE"
            " WHERE City = ('Pune') "
        )
        Query2 = "SELECT * FROM CityArea"

        cursor_comp.execute(
            "CREATE VIEW IF NOT EXISTS MaxSalaryEmp As"
            " SELECT Name,MAX(SALARY),DepartmentId  FROM EMPLOYEE "
            " GROUP BY DepartmentId"
        )

        """Max per department" सारखा निकाल मिळवण्यासाठी SQL मध्ये मूलभूतपणे तीनच मार्ग असतात 
           — GROUP BY, subquery, किंवा window function. यापैकी एकही न वापरता हे शक्य नाही.
        """
        Query3 = "SELECT * FROM MaxSalaryEmp WHERE DepartmentId = ? "

        cursor_comp.execute(
            "CREATE VIEW IF NOT EXISTS DEPTLIST As" " SELECT *  FROM EMPLOYEE "
        )

        # Keys.compnayDB.conn.commit()

        Query4 = ("SELECT * FROM DEPTLIST WHERE DepartmentId = ?")
       
     
        claues.ReadData(cursor_comp, Query4, (1,), "VIEW")

    def DropViwe():
        query = "DROP VIEW DEPTLIST"
        cursor_comp.execute(query)
        Keys.compnayDB.conn.commit()

    @staticmethod
    def ReadData(database, Query, parms, comment):
        print(f"-------------{comment}---------------")
        database.execute(Query, parms)
        # Keys.compnayDB.conn.commit()
        rows = database.fetchall()
        for row in rows:
            print(row)
