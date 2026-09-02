
import json
from pathlib import Path
from ORM_CRUD import CRUDOpertions as StudentCRUD
from ORM_Filter import FilterTable as filter

# StudentCRUD.DropTable()  # Drop the table if it exists


existing_count = StudentCRUD.TableRowsCount()

if existing_count == 0:
    with open(Path(__file__).resolve().parent / "StudInfo.json", "r") as f:
        employees = json.load(f)
    for i, emp in enumerate(employees):
        StudentCRUD.InsertTable(
            _id=i + 1,
            _name=emp["name"],
            _age=emp["age"],
            _gender=emp["gender"],
            _email=emp["email"],
            _DeptID=emp["DeptID"],
        )

# StudentCRUD.UpdateTable(7, 50);
#StudentCRUD.DeleteRow(13)
StudentCRUD.DisplayData()  # Display the data in the table
filter.WhereClause()
