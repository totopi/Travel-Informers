from flask import Flask, render_template, jsonify, redirect

from sqls import city_data
from dfs import timeseries_data, scatter_data, donut_data
app = Flask(__name__)

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

@app.route("/city")
def city():
    data = city_data()
    return jsonify(data)

@app.route("/<city_name>/<month>/<x>")
def give_them_graphs(city_name, month, x):
    traces = []
    if (x == "temp"):
        x = ["daily_avg_temps", "daily_max_temps", "daily_min_temps"]
    elif (x == "wind"):
        x = ["daily_2015_avg_wind", "daily_2015_max_wind", "daily_2015_min_wind"]
    elif (x == "humidity"):
        x = ["daily_2015_avg_humidity", "daily_2015_max_humidity", "daily_2015_min_humidity"]
    traces.append(timeseries_data(city_name, month, x))
    traces.append(scatter_data(city_name, month, x))
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
if __name__ == "__main__":
    app.run(debug=True)