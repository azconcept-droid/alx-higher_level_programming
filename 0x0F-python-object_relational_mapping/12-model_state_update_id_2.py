#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa using sqlalchemy
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # validate input arguments
    if len(argv) != 4:
        print("Usage: {} user passwd database".format(argv[0]))
        exit(1)
    # To connect we use create_engine()
    engine = create_engine('mysql+mysqldb://{}:{}\
    @localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Creating a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get object to be updated
    obj = session.query(State).filter(State.id == 2).first()

    # now modify the name
    obj.name = 'New Mexico'

    # commits the transactions so far
    session.commit()
