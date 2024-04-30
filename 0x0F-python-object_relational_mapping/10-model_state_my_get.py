#!/usr/bin/python3
"""
module that prints a states by id
if state is found else not found
using sqlalchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            f"Usage: {sys.argv[0]} <uname> <paswd> <db_name> <state_name>"
        )
        sys.exit(1)

    uname = sys.argv[1]
    paswd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine and bind it to the session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(uname, paswd, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result or "Not found" if no state matches the name
    if state:
        print(state.id)
    else:
        print("Not found")
