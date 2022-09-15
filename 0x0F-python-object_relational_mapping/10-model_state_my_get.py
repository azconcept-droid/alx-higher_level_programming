#!/usr/bin/python3
"""
prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # validate input arguments
    if len(argv) != 5:
        print("Usage: {} user passwd database state_name".format(argv[0]))
        exit(1)
    # To connect we use create_engine()
    engine = create_engine('mysql+mysqldb://{}:{}\
    @localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Creating a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Quering the the states table where name == passed in argument
    obj = session.query(State).filter(State.name == argv[4]).first()

    if obj:
        print(obj.id)
    else:
        print('Not found')

    # commits the transactions so far
    session.commit()
