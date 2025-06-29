#!/usr/bin/python3

""" The module """

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"
    )

    session = sessionmaker(bind=engine)()

    rows = session.query(State.id, State.name).order_by(State.id)

    for row in rows:
        print(f"{row[0]}: {row[1]}")
