# The application

# Dependencies
from flask import Flask, render_template, jsonify, redirect, request

import json
import random 

# Things from other scripts that are nice
from sqls import city_data, sql_temp_timeseries_data
from dfs import csv_timeseries_data, csv_scatter_data, donut_data

# Usual flask stuff
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
    # data = city_data()
    # data = [x['city_name'] if x['country'] == 'United States' for x in data]
    return render_template("graphs.html")

# @app.route("/graphdata", methods=['GET', 'POST'])
# def graphdata():
#     city = request.form.get('citySelect')
#     month = request.form.get('monthSelect')
#     types = request.form.get('typeSelect')
#     return render_template('graphs2.html', city=city, month=month, types=types)

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
            'tickangle': 90,
            'autotick': False,
            'tick0': 0,
            'dtick': 3
        },
        'yaxis': {
            'title': f'{foo}'
        },
        'autosize': True,
        'plot_bgcolor': '#f1f1f1',
        'paper_bgcolor': '#f1f1f1'
    }
    scatter_layout = {
        'title': f'{foo} vs Number of Airport Delays',
        'xaxis': {
            'title': f'{foo}'
        },
        'yaxis': {
            'title': 'Number of Airport Delays'
        },
        'autosize': True,
        'plot_bgcolor': '#f1f1f1',
        'paper_bgcolor': '#f1f1f1'
    }
    pie_layout = {
        'title': f'Frequency of Weather Conditions in {city_name}',
        'autosize': True,
        'plot_bgcolor': '#f1f1f1',
        'paper_bgcolor': '#f1f1f1'
    }
    traces.append(time_layout)
    traces.append(scatter_layout)
    traces.append(pie_layout)
    return jsonify(traces)

# Let's get some cool picture URLs thanks to Corey Clippinger!
@app.route("/city_pics/<city>")
def get_pic_urls(city):
    # queries the pic urls json file and returns a random sampling of them
    #
    # No guarenttees for trying to get more than 6 pics, so dont' change the random sample selection!!!
    with open('static/data/city_pics_urls.json', 'r') as f:
        data = json.loads(f.read())
        city_urls = data[city]
        return jsonify(random.sample(list(city_urls),6))

@app.route("/pic_collage.html")
def pic_collage():
    return render_template("pic_collage.html")

@app.route("/city_pics/<city>")
def city_collage(city):
    urls = list(get_pic_urls(city))
    return jsonify(urls)
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
if __name__ == "__main__":
    app.run(debug=True)