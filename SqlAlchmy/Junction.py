from sqlalchemy import create_engine


class ORMConnections:
    def __init__(self, db_name):
        try:
            self.engine = create_engine(db_name)
            with self.engine.connect() as conn:  # Actual connection करण्यासाठी:
                print()
                #print("Database connected")
        except Exception as e:
            self.engine = None
            print(f"Database connection failed: {e}")
            # sqlite3 = Python ची SQLite-specific library.
            # SQLAlchemy = अनेक databases साठी abstraction/ORM toolkit.


ORMDB = ORMConnections(
    "sqlite:///SqlAlchmy/School.db"
)  # आपण SQLite database वापरत आहोत.& /// → हा relative path आहे.(current working directory)
