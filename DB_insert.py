
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
engine = create_engine('sqlite:///C:\\myproject\\flights.db')
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open('passenger.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for name, flight_id in csv_reader:
            flights = db.execute("insert into passengers (name, flight_id) VALUES (:name, :flight_id)",{"name":name, "flight_id":flight_id})
            print(f"flight is booked for {name} ")
        db.commit()

if __name__ == "__main__":
    main()
