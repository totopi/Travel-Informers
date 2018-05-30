# Python script to interact with our MySQL database

# Dependencies
import datetime as dt
import numpy as np
import pandas as pd


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pymysql

# I saw this on reddit or stack underflow or wherever, was getting an error if I didn't do it
pymysql.install_as_MySQLdb()

# Create the engine, oh no don't steal all of our SQLs please!
engine = create_engine('mysql://nzc05xl12rgoh7ei:v1h64j9hgv2ky4g1@s3lkt7lynu0uthj8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/x5t20wxo8nmqqxfz')

# Other things that must be done becaues they must be done.  Reminds me of working in Japan
Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

City_attributes = Base.classes.city_attributes
Avg_temp = Base.classes.daily_avg_temps
Max_temp = Base.classes.daily_max_temps
Min_temp = Base.classes.daily_min_temps

temp_list = [Avg_temp, Max_temp, Min_temp]

# Function to get the data needed to populate a Leaflet map, but probably we won't use it in the final product
def city_data():
    city_list = []
    for row in session.query(City_attributes.city, City_attributes.country, City_attributes.abbr, City_attributes.latitude, City_attributes.longitude).all():
        city_list.append({
            "city_name": row[0],
            "country": row[1],
            "city_abbr": row[2],
            "lat": float(row[3]),
            "lon": float(row[4])
        })
    return city_list

# Use our SQL database to return timeseries data for temperatures
def sql_temp_timeseries_data(city, month, files):
    traces = []
<<<<<<< HEAD
    colorlist = ['#aa00cc', '#ff4444', '#4444ff']
=======
    colorlist = ['#aa00aa', '#ff4444', '#4444ff']
>>>>>>> master
    for i in range(3):
        x = []
        y = []
        for row in session.query(getattr(temp_list[i], city), temp_list[i].datetime).filter(temp_list[i].datetime.like(f'%2015-{month}%')).all():
            if (type(row[1]) == str):
                time_converted = dt.datetime.strptime(row[1], '%Y-%m-%d')
                x.append(time_converted)
            elif (type(row[1] == dt.datetime)):
                x.append(row[1])
            y.append(float(row[0]))
        trace = {
            'x': x,
            'y': y,
            'type': 'scatter',
            'name': city + " " + files[i],
            'mode': 'lines',
            'line': {'color': colorlist[i]}
        }
        traces.append(trace)
    return traces