import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine = create_engine('sqlite:///C:\\myproject\\flights.db')
db = scoped_session(sessionmaker(bind=engine))

def main():
    #origin = input("enter origin :")
    passengers = db.execute("select * from passengers")
    #flight = db.execute("select * from flights where origin = :origin",{"origin":origin}).fetchall()
    for p in passengers:
        print(p)

if __name__ == '__main__':
    main()
