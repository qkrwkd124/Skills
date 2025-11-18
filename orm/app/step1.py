from orm.db.db import engine
from orm.models.user import Base, User, Address
from sqlalchemy.orm import Session
from sqlalchemy import select

def create_tables():
    Base.metadata.create_all(engine)

def insert_data():
    with Session(engine) as session:
        
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@squarepants.com")],
        )
        
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@cheeks.com"),
                Address(email_address="sandy@krusty.com")
            ],
        )
        
        patrick = User(
            name="patrick",
            fullname="Patrick Star"
        )

        session.add_all([spongebob, sandy, patrick])
        session.commit()
        
def select_data():
    with Session(engine) as session:
        
        stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
        
        for user in session.scalars(stmt):
            print(user)

def join_select_data():
    with Session(engine) as session:
        stmt = (
            select(Address)
            .join(Address.user)
            .where(User.name == "sandy")
            .where(Address.email_address == "sandy@krusty.com")
        )
        
        sandy_address = session.scalars(stmt).one()
        print(sandy_address)
        
        stmt = select(User).where(User.name == "patrick")
        patrick = session.scalars(stmt).one()
        
        patrick.addresses.append(Address(email_address="patrick@star.com"))
        
        sandy_address.email_address = "sandy_cheeks@krusty.com"
        session.commit()
        

def delete_data():
    with Session(engine) as session:
        stmt = (
            select(Address)
            .join(Address.user)
            .where(User.name == "sandy")
            .where(Address.email_address == "sandy_cheeks@krusty.com")
        )
        
        sandy_address = session.scalars(stmt).one()
        
        sandy = session.get(User, 2)
        sandy.addresses.remove(sandy_address)
        
        session.flush()
        
        patrick = session.get(User, 3)
        session.delete(patrick)
        
        session.commit()
        
if __name__ == "__main__":
    # create_tables()
    # insert_data()
    # select_data()
    # join_select_data()
    delete_data()