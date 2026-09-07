
import json
from pathlib import Path
from enum import Enum
from ORM_CRUD import CRUDOpertions as StudentCRUD
from ORM_Filter import FilterTable
from ORM_Key import Link
from ORM_Join import joins
from SqlAlchmy import ORM_Filter
from typing import Optional




# -----------------------------
# Load JSON
# -----------------------------
existing_count = 0


def load_students_from_json() -> list[dict]:
    json_path = Path(__file__).resolve().parent / "students_10000.json"

    try:
        with open(json_path, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        raise FileNotFoundError(f"Student data file not found at {json_path}")

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {json_path}: {e}")


# -----------------------------
# Seed Data
# -----------------------------


def seed_students_if_empty() -> None:
    global existing_count
    existing_count = StudentCRUD.TableRowsCount()

    print(f"Existing rows: {existing_count}")

    if existing_count == 0:
        students = load_students_from_json()

        StudentCRUD.InsertInBulkRecords(students)

        print("10000 students inserted successfully.")


# -----------------------------
# Enum Menu
# -----------------------------


class Menu(Enum):
    DISPLAY = 1
    UPDATE = 2
    DELETE = 3
    FILTER = 4
    RELATION = 5
    JOIN = 6
    JOIN_FILTER = 7
    LAZY_LOADING = 8
    JOIN_LOAD = 9
    SELECTIN_LOAD = 10
    PAGINATION = 11
    DROP_TABLE = 12
    DBCLEAN=13
    EXIT = 0


# -----------------------------
# Display Menu
# -----------------------------


def display_menu() -> None:

    print("\n========== STUDENT ORM MENU ==========")

    for option in Menu:
        print(f"{option.value}. {option.name.replace('_', ' ').title()}")

    print("=======================================")


# -----------------------------
# Get User Choice
# -----------------------------


def get_choice() -> Optional[Menu]:

    try:
        choice = int(input("Enter your choice: "))

        return Menu(choice)

    except ValueError:
        print("Please enter a valid number.")
        return None


# -----------------------------
# Handle Menu
# -----------------------------


def handle_menu(choice: Menu) -> bool:

    if choice == Menu.DISPLAY:

        StudentCRUD.DisplayData()

    elif choice == Menu.UPDATE:

        student_id = int(input("Enter student ID: "))
        age = int(input("Enter new age: "))

        StudentCRUD.UpdateTable(student_id, age)

    elif choice == Menu.DELETE:

        student_id = int(input("Enter student ID: "))

        StudentCRUD.DeleteRow(student_id)

    elif choice == Menu.FILTER:

        ORM_Filter.FilterCallFunction(None, None)

    elif choice == Menu.RELATION:

        Link.relation()

    elif choice == Menu.JOIN:

        joins.Join()

    elif choice == Menu.JOIN_FILTER:

        joins.joinfilter()

    elif choice == Menu.LAZY_LOADING:

        joins.lazyLoading()

    elif choice == Menu.JOIN_LOAD:

        joins.JoinLoad()

    elif choice == Menu.SELECTIN_LOAD:

        joins.SelectionLoad()

    elif choice == Menu.PAGINATION:
        perpageRecored = 20

        TotalPage = existing_count // perpageRecored
        
        print(f"Total Page in My Book : {TotalPage}")
        
        p_no = int(input("Enter Page Number: "))
        
        ORM_Filter.FilterCallFunction(p_no, perpageRecored)

    elif choice == Menu.DROP_TABLE:

        confirm = input("Are you sure you want to drop the table? (y/n): ").lower()

        if confirm == "y":
            StudentCRUD.DropTable()
        else:
            print("Drop cancelled.")

    elif choice == Menu.DBCLEAN:

     
        confirm = input("Are you sure you want to Database are clean? (y/n): ").lower()

        if confirm == "y":
              ORM_Filter.DBSizeClean()
        else:
            print("clean cancelled.")


    elif choice == Menu.EXIT:

        print("Exiting program...")
        return False

    return True


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" * 10)
