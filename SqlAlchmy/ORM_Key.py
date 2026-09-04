

from Junction import ORMCAR as CARDB
from ORM_Table import Brand, Car
from tabulate import tabulate
from sqlalchemy import select, func, text
from sqlalchemy.orm import Session
from enum import Enum

class BrandLabel():
    toyota="Toyota"
    bmw="BMW"
    hyndai="Hyundai"
    mahindra="Mahindra"
    volkswagen="Volkswagen"


class tableOpertion:
    @staticmethod
    def Insertion():
        try:
            with Session(CARDB.engine) as sesson:

            # First time only: create the brand rows, then commit.
            # After this runs once, keep these commented out.

                # Step 1: Toyota
                # toyota = Brand()
                # toyota.name = "Toyota"
                # toyota.country = "Japan"
                # sesson.add(toyota)
                # sesson.commit()
                
                # Step 2: BMW
                # bmw= Brand(name="BMW",country="Germany")
                # sesson.add(bmw)
                
                # Step 3: Hyundai
                #hyndai = Brand(name="Hyundai", country="South Korea")

                # Step 4: Mahindra
                #mahindra = Brand(name="Mahindra", country="India")

                # Step 4: Volkswagen 
                # volkswagen=Brand(name="Volkswagen", country="Germany") 
                # tableOpertion.InsertionOnCar(sesson,volkswagen)

                #Step 5: Volkswagen 
                # volvo=Brand(name="Volvo", country="Sweden") 
                # tableOpertion.InsertionOnCar(sesson,volvo)

              
            #After brands already exist in the table: fetch by name and insert cars under it
                company = sesson.scalars(select(Brand).where(Brand.name == BrandLabel.volkswagen)).first()
                if company:
                    print(f"Model Is Found: {company}")
                    tableOpertion.InsertionOnCar(sesson,company)
                else:
                    print("Model IS not Found")

            
            print(f"Data Inserted Succesfully")
        except Exception as e:
            print(f"Error Inserting:{e}")
            print(type(e).__name__)

    @staticmethod
    def InsertionOnCar(session, _obj):

        try:
            # Toytoa
            # fortuner = Car(model="Fortuner", price=3500000, brand=_obj)
            # glanza = Car(model="Glanza",price=9500000,brand=_obj)
            #innova = Car(id=12,model="Innova",price=3500000,brand=_obj)
            #vellfire = Car(model="Vellfire",price=1240000,brand=_obj)
            
            
            # BMW
            #m5=Car(model="M5",price=9800000,brand=_obj)
            #z4=Car(model="Z4",price=10000000)
            #x1=Car(model="X1 ",price=12600000,brand=_obj)
            #I5=Car(model="i5 ",price=10000000,brand=_obj)

            #Mahindra
            #thar = Car(model="Thar Roxx", price=200000, brand=_obj)
            #xuv=Car(model="XUV 7XO",price=2500000)#
            #scorpio = Car(model="Scorpio", price=160000, brand=_obj)
             
            #Hyndai
            # grnadi10=Car(model="Grandi10",price=750000, brand=_obj)
            # verana=Car(model="Verana",price=150000, brand=_obj)
            # creta=Car(model="Creta",price=180000, brand=_obj)
            # venue=Car(model="Venue",price=110000, brand=_obj)
           
            #Volkswagen
            #jetta=Car(model="Jetta",price=1450000)
            polo=Car(model="Polo",price=1000000, brand=_obj)


            # alt: append via relationship instead of brand=_obj
            #_obj.cars.append(xuv)
            # alt: group of data insert
            #session.add_all([grnadi10, verana, creta, venue])
            
           
            session.add(polo)

            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error Inserting:{e}")
            print(type(e).__name__)

    @staticmethod
    def ReadTable(TableName):
        with Session(CARDB.engine) as session:
            stmt = select(TableName)
            result = session.scalars(stmt).all()

            if TableName == Brand:
                rows = [[s.id, s.name, s.country] for s in result]
                headers = ["id", "cars", "country"]
            else:
                rows = [[s.id, s.model, s.price, s.brand_id] for s in result]
                headers = ["id", "model", "price", "brand_id"]

            print("\n" + tabulate(rows, headers=headers, tablefmt="grid"))

    def Drops(_tablename):
        with Session(CARDB.engine) as session:
            session.execute(text(f"DROP TABLE IF EXISTS {_tablename}"))
            session.commit()
           
    def Updates(TableName,uData,_id):
        with Session(CARDB.engine) as session:
            row =session.get(TableName,_id)
            if row :
                if TableName is Brand:
                 row.country=uData
                else:
                 row.price=uData

                session.commit()

               
                print(f"Update Succesfully {row}")
            else:
                print(f"Errot : Data is not updated {row}")
                
    def DeleteTables(_tablename,_id):
        with Session(CARDB.engine) as session:
            
            delT = session.scalars(select(_tablename).where(_tablename.id == _id)).first()
            session.delete(delT)
            session.commit()
            
    

class Link:
    def relation():
        # tableOpertion.Insertion()
        #tableOpertion.Drops(Car)
        #tableOpertion.DeleteTables(Car,16)
        #tableOpertion.DeleteTables(Brand,6)

        #tableOpertion.Updates(Brand,"German",5)
        tableOpertion.ReadTable(Brand)
        tableOpertion.ReadTable(Car)