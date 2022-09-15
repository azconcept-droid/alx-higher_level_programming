#!/usr/bin/python3
"""
This script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa using sqlalchemy
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
    # Quering the the states table by inserting
    session.add(State(name="Louisiana"))
    result = session.query(State).filter(State.name == "Louisiana").first()

    print(result.id)

    # commits the transactions so far
    session.commit()
