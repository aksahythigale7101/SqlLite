
from sqlalchemy import func, select, within_group
from sqlalchemy.orm import Session, joinedload, selectinload, session
from Junction import ORMCAR as CARDB
from ORM_Table import Brand, Car


class joins:
    def Join():
        with Session(CARDB.engine) as session:
            #Inner Join
            #rows = session.execute(select(Car, Brand).join(Brand, Car.brand_id == Brand.id))
            #Left Join
            #rows=session.execute(select(Car,Brand).outerjoin(Brand.cars))
            #Right Join
            rows=session.execute(select(Car,Brand).outerjoin(Car.brand))
            # for car,brand    in rows:#Inner Join
            #     print(f"Model : {car.model}      ---- Made in : {brand.country}")
            for car,brand  in rows:
                if car:
                 print(f"Model : {car.model}") 
                else:
                 print(f"Made in : {brand.country}")

                 #
    def joinfilter():
       with Session(CARDB.engine) as session:
           # #rows = session.execute(select(Car).join(Brand).where(Brand.name=="Hyundai",Car.price>90000)).all()
           # for car in rows:
           #  print(car[0].model,car[0].price)
            
           #rows = session.execute(select(Brand.name,func.count(Car.id)).join(Car).group_by(Car.brand_id)
           #                                                     .having(func.count(Car.id)>3)).all()  
                                   
           rows = session.execute(select(Brand.name,func.sum(Car.price)).join(Car).group_by(Car.brand_id)).all()
                                           
           for brand_name, total_price  in rows:
                print(f"{brand_name}: {total_price }")
     
    def lazyLoading():
        with Session(CARDB.engine) as session:
            brands = session.scalars(select(Brand)).all()   # Query 1: सगळे brands
            for brand in brands:
             print(brand.name)
             for car in brand.cars:        # प्रत्येक brand साठी वेगळी query!
                print(" -", car.model)

    def SelectionLoad():
        with Session(CARDB.engine) as session:
         stmt = select(Brand).options(selectinload(Brand.cars))
         brands = session.scalars(stmt).all()
        for brand in brands:
          print(brand.name)
        for car in brand.cars:    # आधीच loaded — नवीन query नाही
            print(" -", car.model)



    def JoinLoad():
        with Session(CARDB.engine) as session:
         stmt = select(Brand).options(joinedload(Brand.cars))
         brands = session.scalars(stmt).unique().all()   # .unique() compulsory!
         for brand in brands:
          print(brand.name)
        for car in brand.cars:
            print(" -", car.model)


