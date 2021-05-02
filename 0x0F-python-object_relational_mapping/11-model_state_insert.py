#!/usr/bin/python3
'''
This script adds the State object “Louisiana” to
the database hbtn_0e_6_usa

'''

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    conn = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(conn.format(argv[1], argv[2],
                                       argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    new_obj = State(name='Louisiana')
    session.add(new_obj)
    session.commit()
    state = session.query(State).filter(State.name == 'Louisiana').first()

    print(state.id)

    session.close()
