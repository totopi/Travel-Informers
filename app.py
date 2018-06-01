# The application

# Dependencies
from flask import Flask, render_template, jsonify, redirect

import json
import random 

# Things from other scripts that are nice
from sqls import city_data, sql_temp_timeseries_data
from dfs import csv_timeseries_data, csv_scatter_data, donut_data, get_pic_urls

# Usual flask stuff
app = Flask(__name__)

# template file routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

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
        foo = "Temperature"
        x = ["Average Temperature", "Maximum Temperature", "Minimum Temperature"]
        traces.append(sql_temp_timeseries_data(city_name, month, x))
        # Then switch it back for the csvs to come
        x = ["daily_avg_temps", "daily_max_temps", "daily_min_temps"]
    elif (x == "wind"):
        foo = "Wind Speed"
        titles = ["Average Wind", "Maximum Wind", "Minimum Wind"]
        x = ["daily_2015_avg_wind", "daily_2015_max_wind", "daily_2015_min_wind"]
        traces.append(csv_timeseries_data(city_name, month, x, titles))
    elif (x == "humidity"):
        foo = "Humidity"
        titles = ["Average Humidity", "Maximum Humidity", "Minimum Humidity"]
        x = ["daily_2015_avg_humidity", "daily_2015_max_humidity", "daily_2015_min_humidity"]
        traces.append(csv_timeseries_data(city_name, month, x, titles))
    # traces.append(csv_timeseries_data(city_name, month, x))  # Doing this in SQL now, but just in case something breaks...
    traces.append(csv_scatter_data(city_name, month, x))
    traces.append(donut_data(city_name, month))
    time_layout = {
        'title': f'{foo} Over Time',
        'xaxis': {
            'tickangle': -75,
            'autotick': False
        },
        'yaxis': {
            'title': f'{foo}'
        }
    }
    scatter_layout = {
        'title': f'{foo} vs Number of Airport Delays',
        'xaxis': {
            'title': f'{foo}'
        },
        'yaxis': {
            'title': 'Number of Airport Delays'
        }
    }
    pie_layout = {
        'title': f'Frequency of Weather Conditions in {city_name}',
        'autosize': True
    }
    traces.append(time_layout)
    traces.append(scatter_layout)
    traces.append(pie_layout)
    return jsonify(traces)

# Let's get some cool picture URLs thanks to Corey Clippinger!
@app.route("/pic_collage.html")
def pic_collage():
    return render_template("pic_collage.html")

@app.route("/city_pics/<city>")
def city_collage(city):
    urls = list(get_pic_urls(city))
    return jsonify(urls)

if __name__ == "__main__":
    app.run(debug=True)