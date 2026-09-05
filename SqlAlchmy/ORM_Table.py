
from encodings import mac_arabic
from Junction import ORMDB as StudentDB,ORMCAR as CARDB
from sqlalchemy import ForeignKey,Index, NotNullable, String, UniqueConstraint, CheckConstraint

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,relationship


class Base(DeclarativeBase): #पण proper SQLAlchemy model बनवण्यासाठी DeclarativeBase वापरतो.
    pass                  #Base is the parent class for our SQLAlchemy models.
                          

class student(Base): #आता Base च्या माध्यमातून आपले models तयार होतील.Model म्हणजे database मधल्या table चे Python representation.
    #def CreateTable():
        __tablename__ = "students"    #Student is a SQLAlchemy ORM model.
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(50))# Mapped[str]Python side → this value is a string.
        age: Mapped[int] = mapped_column()
        gender: Mapped[str] = mapped_column(String(50))
        email: Mapped[str] = mapped_column(String(100), index=True)#, unique=True
        DeptID: Mapped[int] = mapped_column()
        salary: Mapped[float] = mapped_column()
        city: Mapped[str] = mapped_column(String(50))

        __table_args__ = (
        Index("ix_dept_city", "DeptID", "city"),          # composite index 1
        Index("ix_name_age", "name", "age"),               # composite index 2
        Index("ix_gender", "gender"),                      # single-column index
        Index("ix_dept_salary", "DeptID", "salary"),        # composite index 3
        )
# name: Mapped[str] = mapped_column(String(50))
#    ↑                    ↑
# Python type          Database column

Base.metadata.create_all(StudentDB.engine)  # Create the table in the database


class Brand(Base):
    __tablename__= "brands"
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(String(100),nullable=False)
    country:Mapped[str]=mapped_column(String(100),nullable=False)

     # Relationship
    cars:Mapped[list["Car"]] = relationship(back_populates="brand")
   
class Car(Base):
     __tablename__="cars"
     id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
     model:Mapped[str]=mapped_column(String(100),nullable=False)
     price:Mapped[int]=mapped_column()






     brand_id:Mapped[int]=mapped_column(ForeignKey("brands.id"),nullable=False)#cars table मधील brand_id हा brands table मधील id ला refer करतो.
     # Relationship
     brand:Mapped["Brand"]=relationship(back_populates="cars")


Base.metadata.create_all(CARDB.engine)


'''

# region realtionship explaination
    """
     brands.id
        ↑
        |
    cars.brand_id
cars:Mapped[list["Car"]] = relationship(back_populates="brand")
cars          → attribute / variable चे नाव
Mapped        → SQLAlchemy ORM mapping
list["Car"]   → Car objects ची list
relationship  → SQLAlchemy relationship
"brand"       → Car class मधील attribute चे नाव
-------------------------------------------
cars आणि brand तुम्ही मनाप्रमाणे कुठलेही नाव देऊ शकता का?
हो, technically देऊ शकता. पण मग back_populates मध्ये तेच corresponding नाव वापरावे लागेल.
class Brand(Base):
 vehicles: Mapped[list["Car"]] = relationship( back_populates="company")

class Car(Base):
  company: Mapped["Brand"] = relationship(back_populates="vehicles")

  Brand
 └── vehicles  → list of Car objects

Car
 └── company   → one Brand object



"""
    # endregion
'''



