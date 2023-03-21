#!/usr/bin/python3
"""14-model_city_fetch_by_state"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id):
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))
