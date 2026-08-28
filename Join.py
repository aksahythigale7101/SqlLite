



from Keys import keys
import Keys



cursor=Keys.cursor
class _join:
    def innerJoin():
          #query=("SELECT EMPLOYEE.Name, DEPARTMENT.DepartmentName From EMPLOYEE  INNER JOIN DEPARTMENT "
           #               "ON EMPLOYEE.DepartmentId=DEPARTMENT.DepartmentId")
          query1=("SELECT EmployeeId, NAME,DepartmentName FROM EMPLOYEE INNER JOIN DEPARTMENT "
                  "ON EMPLOYEE.DepartmentId=DEPARTMENT.DepartmentId")
          query2=("SELECT  *  FROM EMPLOYEE E INNER JOIN DEPARTMENT D "
                "ON E.DepartmentId = D.DepartmentId")
          
          _join.ReadRows(query1,"INNER JOIN")
         
          # Keys.compnayDB.conn.commit()
          # rows = cursor.fetchall()
          # for x in rows:
          #     print(x)
           
    def LeftJoin():    
         query1=("SELECT E.EmployeeId, E.NAME,D.DepartmentName FROM EMPLOYEE E LEFT JOIN DEPARTMENT D "
                  "ON E.DepartmentId=D.DepartmentId")

         query2=("SELECT E.EmployeeId, E.NAME,D.DepartmentName FROM DEPARTMENT D LEFT JOIN EMPLOYEE E  "
                  "ON E.DepartmentId=D.DepartmentId")

         '''
          query1 and query 2 both are same but ouput is differnt beacuse left side table change query 2 "
         '''
         _join.ReadRows(query2,"LEFT JOIN")


          
    def RightJoin():# version ('3.37.2',) RIGHT and FULL OUTER JOINs are not currently supported
         query1=("SELECT EmployeeId, NAME,DepartmentName FROM EMPLOYEE RIGHT JOIN DEPARTMENT "
                  "ON EMPLOYEE.DepartmentId=DEPARTMENT.DepartmentId")
         #_join.ReadRows(query1,"RIGHT JOIN")
         
         _join.ReadRows("SELECT sqlite_version()","RIGHT JOIN")


    @staticmethod
    def ReadRows(Query,comment):
        print (f"--------------{comment}--------------")
        cursor.execute(Query);
        Keys.compnayDB.conn.commit()
        rows = cursor.fetchall()
        for x in rows:
          print(x)