"""
6. A convenience script to create a user.
Will create the table in DB if not existing already
Can NOT overwrite existing user
create_user.py
-------------
"""

from getpass import getpass
from sqlmodel import SQLModel, Session, create_engine
from schema import User_DBModel


engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},
    echo=True
)


if __name__ == "__main__":
    print("Creating tables (if necessary)")
    SQLModel.metadata.create_all(engine)

    print("-"*20)

    print("This script will create a user and save it in the database.")

    username = input("Please enter username\n")
    pwd = getpass("Please enter password\n")

    with Session(engine) as session:
        user = User_DBModel(username=username)
        user.set_password(pwd)
        session.add(user)
        session.commit()
