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
        <br><br>Temerature Min, Max, and Avg From Selected Dates (Formatted yyyy, mm, dd):\
        <br> /api/v1.0/start_date\
        <br> /api/v1.0/start_date/end_date'


# Percipitation Data
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(bind=engine)
    mm_latest_yr = session.query( measurements.date, measurements.prcp).filter(measurements.date > (dt.date(2016, 8, 23))).all()
    entries = []
    for row in mm_latest_yr:
        entry = {}
        entry["Date"] = row.date
        entry["Percipitation (Inches)"] = row.prcp
        entries.append(entry)
    # Close Session
    session.close()
    return (jsonify(entries))

# Station Data
@app.route("/api/v1.0/stations")
def stations():
    session = Session(bind=engine)
    station_list = session.query(measurements.station).distinct().all()
    entries = []
    for row in station_list:
        entry = {}
        entry["Station"] = row.station
        entries.append(entry)
    # Close Session
    session.close()
    return (jsonify(entries))

# Temperature Data
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(bind=engine)
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
    # Close Session
    session.close()
    return (jsonify(entries))


# Temerature Min, Max, and Avg From Start Date
@app.route("/api/v1.0/<start_date>")
def from_date(start_date):
    session = Session(bind=engine)
    USC00519281_stats = session.query(func.min(measurements.tobs), func.max(measurements.tobs),func.avg(measurements.tobs))\
        .filter_by(station = 'USC00519281')\
        .filter(measurements.date > (start_date)).all()
    entries = []
    for row in USC00519281_stats:
        entry = {}
        entry["Minimum Temperatrue (F)"] = row[0]
        entry["Maximum Temperatrue (F)"] = row[1]
        entry["Average Temperatrue (F)"] = row[2]
        entries.append(entry)
    # Close Session
    session.close()
    return (jsonify(entries))


# Temerature Min, Max, and Avg From Start and End Dates
@app.route("/api/v1.0/<start_date>/<end_date>")
def from_to_date(start_date, end_date):
    session = Session(bind=engine)
    print(start_date)
    print(end_date)
    USC00519281_stats = session.query(func.min(measurements.tobs), func.max(measurements.tobs),func.avg(measurements.tobs))\
        .filter_by(station = 'USC00519281')\
        .filter(measurements.date > (start_date))\
        .filter(measurements.date < (end_date)).all()
    entries = []
    for row in USC00519281_stats:
        print(row)
        entry = {}
        entry["Minimum Temperatrue (F)"] = row[0]
        entry["Maximum Temperatrue (F)"] = row[1]
        entry["Average Temperatrue (F)"] = row[2]
        entries.append(entry)
    # Close Session
    session.close()
    return (jsonify(entries))

# Close Session
session.close()

# App run instructions
if __name__ == "__main__":
    app.run(debug=True)