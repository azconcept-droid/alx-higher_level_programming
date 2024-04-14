#!/usr/bin/python3
"""
This module fetch cities by state
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
    # Quering the the state table use of join
    # it automatically joins mapped classes with foreign keys
    states_cities_obj = session.query(
        State, City
        ).filter(State.id == City.state_id).all()

    for state, city in states_cities_obj:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # commits the transactions so far
    session.commit()
