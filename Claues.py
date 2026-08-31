from ast import Delete
from traceback import print_exception
from unittest import result
from Connection import _Db as studentDB
from Connection import _Db1 as CompanyDB
import Connection
import Keys


cursor_stud = studentDB.conn.cursor()
cursor_comp = CompanyDB.conn.cursor()


class claues:
    def Groupby(self):
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

        Keys.compnayDB.conn.commit()

        Query4 = "SELECT * FROM DEPTLIST WHERE DepartmentId = ?"

        claues.ReadData(cursor_comp, Query4, (3,), "VIEW")

    def DropViwe():
        query = "DROP VIEW DEPTLIST"
        cursor_comp.execute(query)
        Keys.compnayDB.conn.commit()

    def Index():
        NormalIdx = "CREATE INDEX idx_emp_nameColoum" " ON Employee(Name)"

        CompositeIdx = (
            "CREATE INDEX Compoidx_emp_nameColoum" " ON Employee(City,salary)"
        )

        UniqueIdx = (
            "CREATE UNIQUE INDEX Uniqeidx_emp_nameColoum" " ON Employee(EmployeeId)"
        )

        cursor_comp.execute(UniqueIdx)
        Keys.compnayDB.conn.commit()

    def DropIndex():
        query = "DROP INDEX Uniqeidx_emp_nameColoum"
        cursor_comp.execute(query)
        Keys.compnayDB.conn.commit()

    def IsPresentInDB():  # index Or view storge list
        # query=("EXPLAIN QUERY PLAN SELECT * FROM Employee WHERE Name = 'Akshay' ")
        # query = "SELECT name FROM sqlite_master WHERE type = 'index'"
        query = "SELECT name FROM sqlite_master WHERE type = 'trigger'"
        # query=("SELECT name FROM sqlite_schema  WHERE type = 'view'")

        # claues.ReadData(cursor_comp, query, "", "index")
        claues.ReadData(cursor_stud, query, "", "trigger")

    def Triger():
        try:
            insertquery = (
                "CREATE TRIGGER  AfterDeptInsert"
                " AFTER INSERT ON DEPARTMENT"
                " BEGIN"
                " INSERT INTO EMPLOYEE"
                " (EmployeeID,Name,Age,Salary,City,DepartmentId)"
                " VALUES"
                " (112, 'Nidhi', 31, 56000, 'Pune', New.DepartmentId);"
                " END;"
            )

            # cursor_comp.execute(insertquery)
            # CompanyDB.conn.commit()

            UpdateQuery = (
                "CREATE TRIGGER UpdateStud"
                " AFTER UPDATE OF Age ON STUDENTS"
                " BEGIN"
                " INSERT INTO STUDENTS"
                " (Name,Age,Email,Course,enrollment_date)"
                " VALUES"
                " (old.Name,old.Age,'ak@example.com',old.Course,OLD.enrollment_date);"
                " END;"
            )

            DeleteQuery = (
                "CREATE TRIGGER DeleteStud"
                " AFTER DELETE ON STUDENTS"
                " BEGIN"
                " INSERT INTO STUDENTS"
                " (id,Name,Age,Email,Course,enrollment_date)"
                " VALUES"
                "((SELECT MIN(id + 1) "
                "FROM STUDENTS "
                "WHERE (id + 1) NOT IN (SELECT id FROM STUDENTS)), "
                "'Akshay', 31, 'aks@gmail.com', OLD.Course, OLD.enrollment_date); "
                " END;"
            )

            ##Before Insert
            Query1 = (
                "CREATE TRIGGER IF NOT EXISTS CheckStudentAge"
                " BEFORE INSERT ON STUDENTS"
                " WHEN NEW.age < 18"
                " BEGIN"
                " SELECT RAISE(ABORT, 'Student age must be 18 or above');"
                " END;"
            )
            Query2 = (
                "CREATE TRIGGER IF NOT EXISTS CheckStudentAgeUpdate"
                " BEFORE INSERT ON STUDENTS"
                " WHEN NEW.age < 18"
                " BEGIN"
                " SELECT RAISE(ABORT, 'Student age must be 18 or above');"
                " END;"
            )


            cursor_stud.execute(Query2)
            studentDB.conn.commit()

            print("Trigger Successfully Executed")
        except Exception as e:
            print(f"Error Name : {type(e).__name__}")
            print(f"Error Details: {e}")

    def DropTrigger():

        # cursor_stud.execute("PRAGMA database_list")
        # print(cursor_stud.fetchall())

        query = "DROP TRIGGER IF EXISTS DeleteStud"
        # cursor_comp.execute(query)
        # CompanyDB.conn.commit()

        cursor_stud.execute(query)
        studentDB.conn.commit()
        print("Trigger Drop Succedfully")

    @staticmethod
    def ReadData(database, Query, parms, comment):
        print(f"-------------{comment}---------------")
        database.execute(Query, parms)
        # Keys.compnayDB.conn.commit()
        rows = database.fetchall()
        for row in rows:
            print(row)

    @staticmethod
    def NextId():
        cursor_stud.execute(
            """
        SELECT MIN(id + 1)
        FROM STUDENTS
        WHERE (id + 1) NOT IN (SELECT id FROM STUDENTS)
    """
        )

        return cursor_stud.fetchone()[0]
