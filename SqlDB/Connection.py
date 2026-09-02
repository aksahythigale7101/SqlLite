
import os
import sqlite3


class ConnectionDatabase:

    def __init__(self, db_name):
        try:

            db_path = self.find_db_file(db_name)
            self.conn = sqlite3.connect(db_path)

            # print("Database connected successfully.")
        except sqlite3.Error as e:
            self.conn = None
            # print(f"Database connection failed: {e}")

    @staticmethod
    def find_db_file(db_name, search_root=None):
        """
        प्रोजेक्टमध्ये (search_root पासून खाली सगळीकडे) db_name नावाची फाईल शोधतो.
        सापडली तर तिचा पूर्ण (absolute) पाथ परत देतो, नाहीतर None.
        """
        if search_root is None:
            # डिफॉल्ट: या स्क्रिप्टच्या एक फोल्डर वर (प्रोजेक्ट रूट) पासून शोध सुरू करा
            search_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        for root, dirs, files in os.walk(search_root):
            # .venv, .git सारखे मोठे/नको असलेले फोल्डर वगळा
            dirs[:] = [
                d for d in dirs if d not in (".venv", ".git", "__pycache__", ".idea")
            ]

            if db_name in files:
                found_path = os.path.join(root, db_name)
                print(f"Database file '{db_name}' found at: {found_path}")
                return found_path

        return None  # सापडली नाही


# Create the single instance HERE so other files can import it
_Db = ConnectionDatabase("Collage.db")

_Db1 = ConnectionDatabase("Compnay.db")