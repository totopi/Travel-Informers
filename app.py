from flask import Flask, render_template, jsonify, redirect

from city import citydata
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
def maps():
    return render_template("map.html")

@app.route("/timeseries.html")
def timeseries():
    return render_template("timeseries.html")

@app.route("/city")
def city():
    data = citydata()
    return jsonify(data)

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