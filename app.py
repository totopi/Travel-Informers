# The application

# Dependencies
from flask import Flask, render_template, jsonify, redirect
import pandas as pd

from sqls import city_data
from dfs import csv_timeseries_data, csv_scatter_data, donut_data, get_pic_urls
import json
import random 
app = Flask(__name__)

# template file routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/crimedata.html")
def crimedata():
    return render_template("crimedata.html")

@app.route("/hotels.html")
def hotels():
    return render_template("hotels.html")

@app.route("/weather.html")
def weather():
    return render_template("weather.html")


@app.route("/map.html")
def map():
    return render_template("map.html")

@app.route("/chart.html")
def chart():
    return render_template("chart.html")

@app.route("/graphs.html")
def graphs():
    return render_template("graphs.html")

# This route gives you city names, countries, latitudes, and longitudes
@app.route("/city")
def city():
    data = city_data()
    return jsonify(data)

# The big daddy route, gives back 3 sets of [traces] ready to be put straight into Plotly
@app.route("/<city_name>/<month>/<x>")
def give_them_graphs(city_name, month, x):
    traces = []
    if (x == "temp"):
        # but sqlalchemy is a bit funny with variable names and stuff, so...
        x = ["Average Temperature", "Maximum Temperature", "Minimum Temperature"]
        traces.append(sql_temp_timeseries_data(city_name, month, x))
        # Then switch it back for the csvs to come
        x = ["daily_avg_temps", "daily_max_temps", "daily_min_temps"]
    elif (x == "wind"):
        x = ["daily_2015_avg_wind", "daily_2015_max_wind", "daily_2015_min_wind"]
        traces.append(csv_timeseries_data(city_name, month, x))
    elif (x == "humidity"):
        x = ["daily_2015_avg_humidity", "daily_2015_max_humidity", "daily_2015_min_humidity"]
        traces.append(csv_timeseries_data(city_name, month, x))
    # traces.append(csv_timeseries_data(city_name, month, x))
    traces.append(csv_scatter_data(city_name, month, x))
    traces.append(donut_data(city_name, month))
    return jsonify(traces)

'''
@app.route("/scrape")
def scrape():
    # Get the stuff we need to get
    return redirect("//", code=302)

@app.route("/city")
def city():
    # Return weather information for city 

@app.route("/something")
def something():
    # Return something

@app.route("/render")
'''

@app.route("/city_attributes")
def city_attributes():
    df = pd.read_csv("historical-hourly-weather-data/city_attributes.csv", index_col='City')
    print(df.to_dict(orient='records'))
    return jsonify(df.to_dict(orient='records'))

@app.route("/city_pics/<city>")
def city_collage(city):
    urls = list(get_pic_urls(city))
    return jsonify(urls)

if __name__ == "__main__":
    app.run(debug=True)