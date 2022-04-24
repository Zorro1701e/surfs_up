from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# database set up
engine = create_engine("sqlite:///hawaii.sqlite")

# reflecting database
Base = automap_base()

# reflecting the tables
Base.prepare(engine, reflect=True)

#save feference to table to call in LATER. (measurement and station)
measurement = Base.classes.measurement
station = Base.classes.station

# Create session link
session = Session(engine)

app = Flask(__name__)

@app.route('/')

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! <br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

if __name__ =="__main__":
    app.run(debug=True)

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)