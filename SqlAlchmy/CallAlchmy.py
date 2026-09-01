
from Junction import ORMDB as StudentDB
from ORM_Table import student as StudentTable
from ORM_CRUD import CRUDOpertions as StudentCRUD
import json

# Insert Data---------------------------


# StudentCRUD.DropTable()  # Drop the table if it exists


# with open(r"E:\GitProject\SqlLite\SqlAlchmy\StudInfo.json", "r") as f:
#     employees = json.load(f)


# for i, emp in enumerate(employees):
#     StudentCRUD.InsertTable(
#         _id=i+1,
#         _name=emp["name"],
#         _age=emp["age"],
#         _gender=emp["gender"],
#         _email=emp["email"],
#         _DeptID=emp["DeptID"]
#         )

StudentCRUD.DisplayData()  # Display the data in the table
