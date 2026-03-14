from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# AQI using city name
@app.route('/get_aqi/<city>')
def get_aqi(city):

    url = f"https://api.waqi.info/feed/{city}/?token=demo"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        aqi = data["data"]["aqi"]
        return jsonify({
            "city": city,
            "aqi": aqi
        })

    return jsonify({"error": "Data not available"})


# AQI using latitude & longitude (for current location)
@app.route('/get_aqi_location/<lat>/<lon>')
def get_aqi_location(lat, lon):

    url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token=demo"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        aqi = data["data"]["aqi"]
        return jsonify({
            "location": f"{lat},{lon}",
            "aqi": aqi
        })

    return jsonify({"error": "Location AQI not available"})


if __name__ == "__main__":
    app.run(debug=True)