#!/usr/bin/python3
"""
 that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # validate input arguments
    if len(argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py user passwd database")
        exit(1)
    # To connect we use create_engine()
    engine = create_engine('mysql+mysqldb://{}:{}\
    @localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Creating a Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Quering the the state table
    state_obj = session.query(State).order_by(State.id).all()

    for instance in state_obj:
        print('{}: {}'.format(instance.id, instance.name))

    # commits the transactions so far
    session.commit()
