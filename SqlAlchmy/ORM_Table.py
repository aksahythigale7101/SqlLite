
from SqlAlchmy.Junction import ORMDB as StudentDB
from sqlalchemy import String, select

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class student(Base):
    #def CreateTable():
        __tablename__ = "students"
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


