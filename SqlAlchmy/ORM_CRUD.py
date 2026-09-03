
from Junction import ORMDB as StudentDB
from ORM_Table import student as StudentTable
from sqlalchemy.orm import Session

from sqlalchemy import select, func, text
from tabulate import tabulate
from sqlalchemy import update as _update
from sqlalchemy import delete as _delete



class CRUDOpertions:
    def InsertTable(_id, _name, _age, _gender, _email, _DeptID):
        try:
            with Session(
                StudentDB.engine
            ) as session:  # WITH-याचा फायदा म्हणजे काम झाल्यावर session व्यवस्थित close होतो.
                new_student = StudentTable(
                    id=_id,
                    name=_name,
                    age=_age,
                    gender=_gender,
                    email=_email,
                    DeptID=_DeptID,
                )
                session.add(new_student)  # "हा object save करण्यासाठी तयार ठेव."
                session.commit()  # "आता transaction database मध्ये permanently save कर."
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")
            print(type(e).__name__)  # Print the type of the exception

    def TableRowsCount():
        with Session(StudentDB.engine) as session:
            count = session.query(func.count(StudentTable.id)).scalar()
            return count
        
    def UpdateTable(_id, _age):
        try:
            with Session(StudentDB.engine) as session:
                # using get through updatae #by using get फक्त primary key वरून एक record हवा (उदा. ID)
                # stud=session.get(StudentTable,_id)
                # if stud:
                #     stud.age=_age
                #     session.commit()
                # else:
                #      print(f"Session {_id} is not found.")

                # using query through filter and change data
                # stud1=session.query(StudentTable).filter(StudentTable.id==_id).first()
                # stud1.age=_age;
                # session.commit()

                # using scalars
                # scal=select(StudentTable).where(StudentTable.id==_id)
                # stud2=session.scalars(scal).first()
                # stud2.age=_age;
                # session.commit()

                # using normal method and this is not sql alchmy method
                stmt = (
                    _update(StudentTable).where(StudentTable.id == _id).values(age=_age)
                )
                stud3 = session.execute(stmt)
                session.commit()
        except Exception as e:
            print(f"Error updating data: {e}")
            print(type(e).__name__)  # Print the type of the exception

    def DeleteRow(_id):
        try:
            with Session(StudentDB.engine) as session:
                # stud = session.get(StudentTable, _id)
                # if stud:
                #     session.delete(stud)
                #     session.commit()
                #     print(f"Session Deleted : {_id} Successfully.")
                # else:
                #     print(f"Session {_id} is not found.")

                # scal=select(StudentTable).where(StudentTable.id==_id)
                # stud2=session.scalars(scal).first()
                # session.delete(stud2)
                # session.commit()

                stmt = (
                    _delete(StudentTable).where(StudentTable.id == _id)
                )
                stud3 = session.execute(stmt)
                session.commit()



                session.commit()

        except Exception as e:
            print(f"Error updating data: {e}")
            print(type(e).__name__)  # Print the type of the exception

    def DropTable():
        try:
            with Session(StudentDB.engine) as session:
                session.execute(text("DROP TABLE IF EXISTS students"))
                session.commit()
                print("Table dropped successfully.")
        except Exception as e:
            print(f"Error dropping table: {e}")
            print(type(e).__name__)  # Print the type of the exception

    def DisplayData():
        try:
            with Session(StudentDB.engine) as session:
                Stud = session.query(StudentTable).all()

                rows = [
                    [s.id, s.name, s.age, s.gender, s.email, s.DeptID] for s in Stud
                ]
                headers = ["ID", "Name", "Age", "Gender", "Email", "DeptID"]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
                # for student in rows:
                #     print(
                #         f"ID:   {student.id}, Name: {student.name}, Age: {student.age }"
                #         f", Gender: {student.gender}, Email: {student.email}, DeptID: {student.DeptID}"
                #     )
        except Exception as e:
            print(f"Error displaying data: {e}")
            print(type(e).__name__)  # Print the type of the exception

            # -------------------------------------------------------------------------------------------------------------------------------------------------
            # region this recore display method
            """
            stnt = select(StudentTable).where(StudentTable.id == 5)
                r = session.scalars(stnt)#वापरल्यावर तो automatically tuple मधून पहिला element काढून देतो
                # print(st[2].email)
                # ro = r.first()#.first() वापरून तुम्हाला त्यातला फक्त पहिला result मिळतो.
                # ro = r.one()#.one() तेव्हाच वापरा जेव्हा तुम्हाला खात्री आहे की query मधून फक्त एकच result येईल — उदा. id किंवा email सारख्या unique column वर filter करताना:
               #print(ro.name)
                print("-------------")

                stnt1 = select(StudentTable.name, StudentTable.age)
                result = session.execute(stnt1)#.execute() वापरल्यावर प्रत्येक row Row object (tuple सारखं) स्वरूपात मिळतो
                # for row in result:
                #     print(row)

                print("-------------")
            """
            # endregion