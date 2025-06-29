#!/usr/bin/python3

""" The module """

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    )

    session = sessionmaker(bind=engine)()

    state = session.query(State.id).where(State.name == sys.argv[4]).first()

    if state:
        print(state[0])
    else:
        print("Not found")
