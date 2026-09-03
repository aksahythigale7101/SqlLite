
from pyexpat import model
from Junction import ORMCAR as CARDB
from ORM_Table import Brand, Car
from tabulate import tabulate
from sqlalchemy import select, func, text
from sqlalchemy.orm import Session


class tableOpertion:
    @staticmethod
    def Insertion():
        try:
            with Session(CARDB.engine) as sesson:

                # Step 1:
                # toyota = Brand()
                # toyota.name = "Toyota"
                # toyota.country = "Japan"
                # sesson.add(toyota)
                # sesson.commit()

                # _toyota = sesson.scalars(select(Brand).where(Brand.name == "Toyota")).first()
                # if _toyota:
                #     print("Model Is Found")
                #     tableOpertion.InsertionOnCar(sesson,_toyota)
                # else:
                #     print("Model IS not Found")

                """
                #Step 2:
                bmw= Brand(
                    name="BMW",
                    country="Germany"
                )
                sesson.add(bmw)
                """
                # _bmw = sesson.scalars(select(Brand).where(Brand.name == "BMW")).first()
                # tableOpertion.InsertionOnCar(sesson,_bmw)

                # mahindra = Brand(name="Mahindra", country="India")
                # tableOpertion.InsertionOnCar(sesson, mahindra)


                hyndai = Brand(name="Hyundai", country="South Korea")
                tableOpertion.InsertionOnCar(sesson, hyndai)
                
                print(f"Data Inserted Succesfully")

        except Exception as e:
            print(f"Error Inserting:{e}")
            print(type(e).__name__)

    @staticmethod
    def InsertionOnCar(session, _obj):
        # with Session(CARDB.engine) as sesson:#नवीन session (session 2) उघडतोस आणि त्या नवीन session मध्ये _toyota object वापरून Car बनवतोस.
        try:
            # Toytoa
            # fortuner = Car(model="Fortuner", price=3500000, brand=_obj)
            # glanza = Car(model="Glanza",price=9500000,brand=_obj)

            # BMW
            #m5=Car(model="M5",price=9800000,brand=_obj)
            #z4=Car(model="Z4",price=10000000)
            #Mahindra
            #thar = Car(model="Thar Roxx", price=200000, brand=_obj)

            #Hyndai
            grnadi10=Car(model="Grandi10",price=750000, brand=_obj)
            verana=Car(model="Verana",price=150000, brand=_obj)
            creta=Car(model="Creta",price=180000, brand=_obj)
            venue=Car(model="Venue",price=110000, brand=_obj)
           


           
            # _obj.cars.append(z4)
            # session.add(z4)
            
            session.add_all([grnadi10, verana, creta, venue])




            session.commit()
        except Exception as e:
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
           

    def DeleteTables(_tablename):
        with Session(CARDB.engine) as session:
            
            delT = session.scalars(select(_tablename).where(_tablename.id == 4)).first()
            session.delete(delT)
            session.commit()

class Link:
    def relation():
        tableOpertion.Insertion()
        #tableOpertion.Drops(Car)
        #tableOpertion.DeleteTables(Brand)
        tableOpertion.ReadTable(Brand)
        tableOpertion.ReadTable(Car)