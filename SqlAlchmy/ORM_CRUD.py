from ORM_Table import student as StudentTable
from Junction import ORMDB as StudentDB
from sqlalchemy.orm import Session

from sqlalchemy import text
from tabulate import tabulate

class CRUDOpertions:
    def InsertTable(_id, _name, _age, _gender, _email, _DeptID):
        try:
            with Session(StudentDB.engine) as session:
                new_student = StudentTable(
                    id=_id,
                    name=_name,
                    age=_age,
                    gender=_gender,
                    email=_email,
                    DeptID=_DeptID,
                )
                session.add(new_student)
                session.commit()
            print("Data inserted successfully.")
        except Exception as e:
            print(f"Error inserting data: {e}")
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
                rows = [[s.id, s.name, s.age, s.gender, s.email, s.DeptID] for s in Stud]
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