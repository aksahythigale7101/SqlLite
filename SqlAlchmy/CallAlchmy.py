import json
from pathlib import Path
from shlex import join

from sqlalchemy import orm
from ORM_CRUD import CRUDOpertions as StudentCRUD
from ORM_Filter import FilterTable 
from ORM_Key import Link
from ORM_Join import joins
from SqlAlchmy import ORM_Filter






def load_students_from_json() -> list[dict]:
    json_path = Path(__file__).resolve().parent / "students_10000.json"
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Student data file not found at {json_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {json_path}: {e}")


def seed_students_if_empty() -> None:
    existing_count = StudentCRUD.TableRowsCount()
    print(f"Existing rows: {existing_count}")
    if existing_count == 0:
        students = load_students_from_json()
        #[StudentCRUD.InsertTable(_id=s["id"], _name=s["name"], _age=s["age"], _gender=s["gender"], _email=s["email"],
                                        #_DeptID=s["DeptID"], _salary=s["salary"], _city=s["city"]) for s in students]#vs 5-10 min row-by-row
        StudentCRUD.InsertInBulkRecords(students)  # bulk insert: ~3-5 sec 



def main() -> None:
    seed_students_if_empty()
    #StudentCRUD.DisplayData()

    # --- Optional demo calls (uncomment as needed) ---
    # StudentCRUD.DropTable()
    # StudentCRUD.UpdateTable(7, 50)
    # StudentCRUD.DeleteRow(13)
    ORM_Filter.FilterCallFunction()
    # Link.relation()
    # joins.Join()
    # joins.joinfilter()
    # joins.lazyLoading()
    # joins.JoinLoad()
    # joins.SelectionLoad()


if __name__ == "__main__":
    main()

