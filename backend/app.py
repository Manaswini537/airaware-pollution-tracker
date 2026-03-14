from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route (fixes 404)
@app.route("/")
def home():
    return "AirAware Pollution Tracker API is running!"

# Get AQI by city
@app.route('/get_aqi/<city>')
def get_aqi(city):

    url = f"https://api.waqi.info/feed/{city}/?token=demo"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        return jsonify({
            "city": city,
            "aqi": data["data"]["aqi"]
        })

    return jsonify({"error": "Data not available"})

# Get AQI using latitude & longitude
@app.route('/get_aqi_location/<lat>/<lon>')
def get_aqi_location(lat, lon):

    url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token=demo"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        return jsonify({
            "location": f"{lat},{lon}",
            "aqi": data["data"]["aqi"]
        })

    return jsonify({"error": "Location AQI not available"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)