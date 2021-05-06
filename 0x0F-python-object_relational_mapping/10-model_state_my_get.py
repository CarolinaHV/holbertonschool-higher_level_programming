#!/usr/bin/python3
'''
This script prints the State object with the name
passed as argument from the database hbtn_0e_6_usa

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

    for state in session.query(State).order_by(State.id).all():
        if argv[4] == state.name:
            print(state.id)
            session.close()
            sys.exit()

    print("Not found")

    session.close()