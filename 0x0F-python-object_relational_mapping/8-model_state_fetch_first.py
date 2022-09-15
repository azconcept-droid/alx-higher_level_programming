#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
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
    # Quering the the states table
    first_row = session.query(State).order_by(State.id).first()

    if first_row:
        print('{}: {}'.format(first_row.id, first_row.name))
    else:
        print('Nothing')

    # commits the transactions so far
    session.commit()
