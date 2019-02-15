import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from flask import Flask, render_template, request, session, redirect, url_for
from models import *

app = Flask(__name__)
"""
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\myproject\\flights.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
"""

engine = create_engine('sqlite:///C:\\myproject\\flights.db')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("select * from flights")
    return render_template("index.html", flights=flights)
@app.route("/book" , methods=["POST"])
def book():
        name = request.form.get("name")
        if name is "":
            return render_template("error.html", message="Please select the valid name!!!")
        try:
            flight_id = int(request.form.get("flight_id"))
        except ValueError:
            return render_template("error.html", message="Please select the valid flight!!!")
        if db.execute("select * from flights where id=:id",{"id":flight_id}).rowcount == 0:
            return render_template("error.html", message="Flight does not exist!!!")
        db.execute("insert into passengers (name, flight_id) VALUES (:name, :flight_id)",{"name":name, "flight_id":flight_id})
        db.commit()
        return render_template("success.html", message="flight booked successfully!!!")

@app.route("/flight/")
def flight():
    flights = db.execute("select * from flights")
    return render_template("flight.html", flights=flights)

@app.route("/flight/<int:flight_id>")
def flights(flight_id):
    flight_detail = db.execute("select * from flights where id=:id",{"id":flight_id}).fetchone()
    if flight_detail is None:
        return render_template("error.html", message="Flight does not exist!!!")
    passenger_detail = db.execute("select name from passengers where flight_id=:flight_id",{"flight_id":flight_id}).fetchall()

    return render_template("flights.html", passenger_detail=passenger_detail, flight_detail=flight_detail)

