import json
from pathlib import Path

from sqlalchemy import orm
from ORM_CRUD import CRUDOpertions as StudentCRUD
from ORM_Filter import FilterTable 
from ORM_Key import Link
from ORM_Join import joins
from SqlAlchmy import ORM_Filter
from funcAssgine import display_menu,get_choice,handle_menu,seed_students_if_empty,clear_console


def main() -> None:

    

    seed_students_if_empty()

    while True:
        #clear_console()
        display_menu()

        choice = get_choice()

        if choice is None:
            input("\nInvalid choice. Press Enter...")
            continue

        if not handle_menu(choice):
            break
        
        input("\nPress Enter to continue...")

# -----------------------------
# Program Start
# -----------------------------

if __name__ == "__main__":
    main()


