#!/usr/bin/python3

""" The module """

from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
    )
    session = sessionmaker(bind=engine)()

    rows = (session.query(City, State)
            .join(State, City.state_id == State.id)
            .order_by(City.id))

    for city, state in rows:
        print(f"{state.name}: ({city.id}) {city.name}")
