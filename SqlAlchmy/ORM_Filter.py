from Junction import ORMDB as StudentDB
from ORM_Table import student as StudentTable
from sqlalchemy import  select,or_,and_,not_,func
from sqlalchemy.orm import Session
from tabulate import tabulate


class FilterTable:
    def WhereClause(session):
        #with Session(StudentDB.engine) as session:
            stmt1 = select(StudentTable).where(StudentTable.age > 30)
            stmt2 = select(StudentTable).where(StudentTable.name == "Sneha Patil")
            stmt3 = select(StudentTable).where(StudentTable.age <= 25)
            stmt4 = select(StudentTable).where(StudentTable.gender != "Male")
            stmt5 = select(StudentTable).where(StudentTable.gender != "Female",StudentTable.age>35)##and
            stmt6 = select(StudentTable).where(and_(StudentTable.name == "Pooja Reddy",StudentTable.id==10))#and
            stmt7 = select(StudentTable).where(or_(StudentTable.gender == "Female",StudentTable.id==10))#or
            stmt8 = select(StudentTable).where(StudentTable.id.in_([1,5,15]))#in
            stmt9 = select(StudentTable).where(StudentTable.name.like('p%'))#like contains %p%
            stmt10 =select(StudentTable).where(StudentTable.DeptID.between(3,5))
            stmt11 =session.query(StudentTable).filter(not_(StudentTable.gender == "Male"))
            ###
            stmt12 = select(StudentTable).order_by(StudentTable.age.desc())
            ###
            stmt13 = select(StudentTable).limit(4)#first 4
            stmt14 = select(StudentTable).offset(4)#skip then 4
            stmt15 = select(StudentTable).offset(4).limit(6)

            stmt16 =select(StudentTable).where(StudentTable.DeptID==1)

            result = session.scalars(stmt16).all()
            
            FilterTable.Showdata(result, "WHERE")
                
    def Group_Haveing(session):
         stmt1 = select(StudentTable.gender, func.count(StudentTable.gender)).group_by(StudentTable.gender)
         stmt2 = select(StudentTable.age,StudentTable.name).where(StudentTable.age>select(func.avg(StudentTable.age)))
         stmt3 = select(StudentTable.DeptID,StudentTable.gender, func.count(StudentTable.gender)).group_by(StudentTable.DeptID,StudentTable.gender)                
         stmt4 = select(StudentTable.DeptID,func.count(StudentTable.DeptID)).group_by(StudentTable.DeptID).having(func.count(StudentTable.DeptID)==1)                       
         stmt5 = select(StudentTable.DeptID,func.Min(StudentTable.age)).group_by(StudentTable.DeptID).having(func.Min(StudentTable.age)>25)                       
         stmt6 = select(StudentTable.DeptID,func.count(StudentTable.id)).where(StudentTable.gender=="Male") .group_by(StudentTable.DeptID).having(func.count(StudentTable.id)>2)     
                                                           
         #result = session.scalars(stmt2).all()
         result = session.execute(stmt6).all()
         for i in result:
          print(i)
         
         
       
    @staticmethod
    def Showdata(_result, comment):
        print(
            f"______________________________________{comment}________________________________________"
        )
        # for student in student:
        #     print(
        #         f"{student.id},  {student.name},   {student.age }  "
        #         f",{student.gender},  {student.DeptID}"
        #     )
        rows = [[s.id, s.name, s.age, s.gender, s.email, s.DeptID] for s in _result]
        headers = ["ID", "Name", "Age", "Gender", "Email", "DeptID"]
        print(tabulate(rows, headers=headers, tablefmt="grid"))



def FilterCallFunction():
    try:
        with Session(StudentDB.engine) as session:
            FilterTable.WhereClause(session)
            FilterTable.Group_Haveing(session)
    finally:
           session.close





