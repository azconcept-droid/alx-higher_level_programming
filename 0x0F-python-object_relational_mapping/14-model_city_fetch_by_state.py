#!/usr/bin/python3
"""

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
    states_cities_obj = session.query(
        State, City
        ).filter_by(State.id == City.state_id).all()

    for state, city in states_cities_obj:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # commits the transactions so far
    session.commit()
