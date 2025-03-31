from flask import Flask, jsonify, request
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Rota inicial
@app.route("/")
def home():
    return jsonify({
        "message": "API NASA - Endpoints disponíveis:",
        "endpoints": {
            "/apod": "Astronomy Picture of the Day",
            "/mars-photos": "Fotos do Mars Rover",
            "/neo": "Dados de Near-Earth Objects"
        }
    })

# Astronomy Picture of the Day
@app.route("/apod")
def get_apod():
    date = request.args.get("date", "")
    
    params = {
        "api_key": app.config["NASA_API_KEY"],
        "date": date if date else None
    }
    
    try:
        response = requests.get(
            f"{app.config['BASE_URL']}/planetary/apod",
            params=params
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 400

# Fotos do Mars Rover
@app.route("/mars-photos")
def get_mars_photos():
    rover = request.args.get("rover", "curiosity")
    sol = request.args.get("sol", 1000)  # Dia marciano
    
    url = f"{app.config['BASE_URL']}/mars-photos/api/v1/rovers/{rover}/photos"
    
    params = {
        "api_key": app.config["NASA_API_KEY"],
        "sol": sol
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 400

# Near-Earth Objects
@app.route("/neo")
def get_neo():
    start_date = request.args.get("start_date", "2023-09-01")
    
    url = f"{app.config['BASE_URL']}/neo/rest/v1/feed"
    
    params = {
        "api_key": app.config["NASA_API_KEY"],
        "start_date": start_date
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)