import os
from sqlalchemy import create_engine


class ORMConnections:

    def __init__(self, db_name, db_folder=None):
        try:
            self.db_folder = db_folder
            db_path = self.find_db_file(db_name)

            if db_path is None:
                # सापडली नाही → दिलेल्या फोल्डरमध्ये नवीन फाईल तयार करा
                os.makedirs(self.db_folder, exist_ok=True)
                db_path = os.path.join(self.db_folder, db_name)
                print(f"'{db_name}' not found, creating new file at: {db_path}")


            db_path = db_path.replace("\\", "/")

            db_url = f"sqlite:///{db_path}"  # SQLAlchemy साठी बरोबर URL तयार करा
            # print("Using URL:", db_url)

            self.engine = create_engine(db_url)
            with self.engine.connect() as conn:  # Actual connection करण्यासाठी:
                # print("Actual path used:", os.path.abspath(db_name))

                print("Database connected")

        except Exception as e:
            self.engine = None
            print(
                f"Database connection failed: {e}"
            )  # sqlite3 = Python ची SQLite-specific library.# SQLAlchemy = अनेक databases साठी abstraction/ORM toolkit.

    @staticmethod
    def find_db_file(db_name, search_root=None):
        search_root = search_root or os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
        for root, dirs, files in os.walk(search_root):
            dirs[:] = [
                d for d in dirs if d not in (".venv", ".git", "__pycache__", ".idea")
            ]
            if db_name in files:
                return os.path.join(root, db_name)
        return None


ORMDB = ORMConnections("School.db")  # आपण SQLite database वापरत आहोत.& /// → हा relative path आहे.(current working directory)# "sqlite:///School.db"


#path= r"E:\GitProject\SqlLite\SqlAlchmy"
ORMCAR = ORMConnections("Vehicles.db")