from flask import Flask, render_template, jsonify, redirect
<<<<<<< HEAD
import pandas as pd
=======
>>>>>>> chrisprabhu

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
<<<<<<< HEAD
=======

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
>>>>>>> chrisprabhu
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
<<<<<<< HEAD
@app.route("/city_attributes")
def city_attributes():
    df = pd.read_csv("historical-hourly-weather-data/city_attributes.csv", index_col='City')
    print(df.to_dict(orient='records'))
    return jsonify(df.to_dict(orient='records'))


=======
>>>>>>> chrisprabhu
if __name__ == "__main__":
    app.run(debug=True)