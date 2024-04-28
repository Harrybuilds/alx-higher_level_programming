#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            f"Usage: {sys.argv[0]} <username> <password> <database_name>"
        )
        sys.exit(1)

    uname = sys.argv[1]
    paswd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and bind it to the session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(uname, paswd, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%'))

    starts = states_with_a.order_by(State.id).all()

    # Print the results
    for state in starts:
        print("{}: {}".format(state.id, state.name))
