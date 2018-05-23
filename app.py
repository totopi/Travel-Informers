from flask import Flask, render_template, jsonify, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
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