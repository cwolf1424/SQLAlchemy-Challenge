# Import the dependencies.

# Import Flask
from flask import Flask, jsonify

#Import Datetime
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################

# Setup engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
# Reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
measurements = Base.classes.measurement
stations = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

#Start at the homepage.
@app.route("/")
def home():
    #List all the available routes.
    return f'Welcome to the Hawaii Weather API!\
        <br>---------------------------------------------------\
        <br><br> Available routes:\
        <br><br> Precipitation Data:\
        <br> /api/v1.0/precipitation\
        <br><br>Station Data:\
        <br> /api/v1.0/stations\
        <br><br>Temperature Data:\
        <br> /api/v1.0/tobs\
        <br><br>Temerature Min, Max, and Avg From Selected Dates:\
        <br> /api/v1.0/start_date\
        <br> /api/v1.0/start_date/end_date'


# Percipitation Data
@app.route("/api/v1.0/precipitation")
def precipitation():
    mm_latest_yr = session.query( measurements.date, measurements.prcp).filter(measurements.date > (dt.date(2016, 8, 23))).all()
    entries = []
    for row in mm_latest_yr:
        entry = {}
        entry["Date"] = row.date
        entry["Percipitation (Inches)"] = row.prcp
        entries.append(entry)
    return (jsonify(entries))

# Station Data
@app.route("/api/v1.0/stations")
def stations():
    station_count = session.query(measurements.station).distinct()
    entries = []
    for row in station_count:
        entry = {}
        entry["Station"] = row.station
        entries.append(entry)
    return (jsonify(entries))

# Temperature Data
@app.route("/api/v1.0/tobs")
def tobs():
    USC00519281_last_yr = session.query(measurements.date, measurements.tobs)\
        .filter(measurements.date > (dt.date(2016, 8, 18)))\
        .filter_by(station="USC00519281")\
        .order_by(measurements.date).all()
    entries = []
    for row in USC00519281_last_yr:
        entry = {}
        entry["Date"] = row.date
        entry["Temperature (F)"] = row.tobs
        entries.append(entry)
    return (jsonify(entries))

# Temerature Min, Max, and Avg From Start Date
@app.route("/api/v1.0/start_date")
def from_date():
    return f'Nothing here yet!'

# Temerature Min, Max, and Avg From Start and End Dates
@app.route("/api/v1.0/start_date/end_date")
def from_to_date():
    return f'Nothing here yet!'

session.close()

if __name__ == "__main__":
    app.run(debug=True)