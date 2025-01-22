#Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify, request


# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Establishing home route
@app.route("/")
def home():
    return (
        f"<center><h2>Welcome to the Hawaii Climate Analysis API!</h2></center>"
        f"<center><h3>Select from one of the available routes:</h3></center>"
        f"<center>Available Routes:<br/></center>"
        f"<center>/api/v1.0/precipitation</center>"
        f"<center>/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MM/DD/YYYY.</p>"
        
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previousYear).all()

    session.close()
    precip = {date:prcp for date, prcp in results} 
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    session.close

    stationList = list(np.ravel(results))
    return jsonify(stationList)


@app.route("/api/v1.0/tobs")
def tobs():
    previousYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= previousYear).all()
    
    session.close()

    temperatureList = list(np.ravel(results))
    return jsonify(temperatureList)

@app.route("/api/v1.0/temp/<start>/<end>")
def dateStats(start=None, end=None):

    selection = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
                 
    if not end:
        startDate = dt.datetime.strptime(start, "%m%d%Y")

        results = session.query(*selection).filter(Measurement.date >=startDate).all()

        session.close

        dateList = list(np.ravel(results))

        return jsonify(dateList)

    else:
        startDate = dt.datetime.strptime(start, "%m%d%Y")
        endDate = dt.datetime.strptime(end, "%m%d%Y")

        results = session.query(*selection).filter(Measurement.date >=startDate).all()
       
        session.close

        dateList = list(np.ravel(results))

        return jsonify(dateList)

# App launcher
if __name__ == '__main__':
    app.run(debug=True)