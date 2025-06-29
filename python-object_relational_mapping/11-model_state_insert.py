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

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    state = session.query(State.id).where(State.name == 'Louisiana').first()

    print(state[0])
