
from Junction import ORMDB as StudentDB
from sqlalchemy import String

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase): #पण proper SQLAlchemy model बनवण्यासाठी DeclarativeBase वापरतो.
    pass                  #Base is the parent class for our SQLAlchemy models.
                          

class student(Base): #आता Base च्या माध्यमातून आपले models तयार होतील.Model म्हणजे database मधल्या table चे Python representation.
    #def CreateTable():
        __tablename__ = "students"    #Student is a SQLAlchemy ORM model.
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(
            String(50)
        )  # Mapped[str]Python side → this value is a string.
        age: Mapped[int] = mapped_column()
        gender: Mapped[str] = mapped_column(String(10))
        email: Mapped[str] = mapped_column(String(100))
        DeptID: Mapped[int] = mapped_column()


# name: Mapped[str] = mapped_column(String(50))
#    ↑                    ↑
# Python type          Database column

Base.metadata.create_all(StudentDB.engine)  # Create the table in the database


