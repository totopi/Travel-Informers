import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pymysql
pymysql.install_as_MySQLdb()

engine = create_engine('mysql://nzc05xl12rgoh7ei:v1h64j9hgv2ky4g1@s3lkt7lynu0uthj8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/x5t20wxo8nmqqxfz')

Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)

City_attributes = Base.classes.city_attributes
def citydata():
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