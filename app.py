import requests
from flask import Flask, render_template, request
from datetime import datetime
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)
app.debug = False


def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Radius of Earth in kilometers
    radius = 6371.0

    # Calculate the distance
    distance = radius * c

    return distance


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        current_weather_url = "https://api.weatherapi.com/v1/current.json?&key=936d1a05cd2042888d8163644241601&q={}&aqi=yes"
        forecast_url = "http://api.weatherapi.com/v1/forecast.json?key=936d1a05cd2042888d8163644241601&q={}&days=4&aqi=yes&alerts=no"
        geocoding_url = "https://api.opencagedata.com/geocode/v1/json?q={}%2C{}&key=c78bc621f5d74ecbb3eb86bd62a68024"

        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        city_input = request.form.get("city")

        if city_input:
            city = city_input
        elif latitude and longitude:
            geocode_response = requests.get(geocoding_url.format(latitude, longitude)).json()
            if "results" in geocode_response:
                city = geocode_response["results"][0]["components"]["district"]
        else:
            error_message = "Invalid Input"
            return render_template("weather.html", error_message=error_message)


        #______________________________ Current Weather ______________________________#

        weather_response = requests.get(current_weather_url.format(city)).json()

        if "current" in weather_response and city_input is not None:
            current_EPA_index = weather_response["current"]["air_quality"]["us-epa-index"]

            if current_EPA_index == 1:
                current_EPA_index = "Good"
            elif current_EPA_index == 2:
                current_EPA_index = "Moderate"
            elif current_EPA_index == 3:
                current_EPA_index = "Unhealthy for sensitive group"
            elif current_EPA_index == 4:
                current_EPA_index = "Unhealthy"
            elif current_EPA_index == 5:
                current_EPA_index = "Very Unhealthy"
            elif current_EPA_index == 6:
                current_EPA_index = "Hazardous"

            datetime_str = weather_response["location"]["localtime"]
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
            date_only = datetime_obj.strftime("%Y-%m-%d")

            weather_data = {
                "day": datetime.strptime(date_only, "%Y-%m-%d").strftime("%A"),
                "date" : date_only,
                "city": weather_response["location"]["name"],
                "country": weather_response["location"]["country"],
                "temperature": weather_response["current"]["temp_c"],
                "description": weather_response["current"]["condition"]["text"],
                "icon": weather_response["current"]["condition"]["icon"],
                "air_quality": current_EPA_index,
            }



        #______________________________ Forecast Weather ______________________________#

            forecast_response = requests.get(forecast_url.format(city)).json()

            forecast_data = []
            for daily_data in forecast_response["forecast"]["forecastday"][1:4]:

                forecast_data.append({
                    "day": datetime.strptime(daily_data["date"], "%Y-%m-%d").strftime("%A"),
                    "max_temp": daily_data["day"]["maxtemp_c"],
                    "min_temp": daily_data["day"]["mintemp_c"],
                    "description": daily_data["day"]["condition"]["text"],
                    "icon": daily_data["day"]["condition"]["icon"],
                })

            return render_template("weather.html", current=weather_data, forecast=forecast_data)

        else:
            error_message = "Invalid City"
            return render_template("weather.html", error_message=error_message)


    else:
        current_weather_KL = requests.get("https://api.weatherapi.com/v1/current.json?&key=936d1a05cd2042888d8163644241601&q=kuala%20lumpur&aqi=yes").json()
        forecast_weather_KL = requests.get("http://api.weatherapi.com/v1/forecast.json?key=936d1a05cd2042888d8163644241601&q=kuala%20lumpur&days=4&aqi=yes&alerts=no").json()


         #______________________________ Current Weather ______________________________#

        current_EPA_index = current_weather_KL["current"]["air_quality"]["us-epa-index"]

        if current_EPA_index == 1:
            current_EPA_index = "Good"
        elif current_EPA_index == 2:
            current_EPA_index = "Moderate"
        elif current_EPA_index == 3:
            current_EPA_index = "Unhealthy for sensitive group"
        elif current_EPA_index == 4:
            current_EPA_index = "Unhealthy"
        elif current_EPA_index == 5:
            current_EPA_index = "Very Unhealthy"
        elif current_EPA_index == 6:
            current_EPA_index = "Hazardous"

        datetime_str = current_weather_KL["location"]["localtime"]
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        date_only = datetime_obj.strftime("%Y-%m-%d")

        weather_data = {
            "day": datetime.strptime(date_only, "%Y-%m-%d").strftime("%A"),
            "date" : date_only,
            "city": "Kuala Lumpur",
            "country": "Malaysia",
            "temperature": current_weather_KL["current"]["temp_c"],
            "description": current_weather_KL["current"]["condition"]["text"],
            "icon": current_weather_KL["current"]["condition"]["icon"],
            "air_quality": current_EPA_index,
        }


        #______________________________ Forecast Weather ______________________________#

        forecast_data = []
        for daily_data in forecast_weather_KL["forecast"]["forecastday"][1:4]:

            forecast_data.append({
                "day": datetime.strptime(daily_data["date"], "%Y-%m-%d").strftime("%A"),
                "max_temp": daily_data["day"]["maxtemp_c"],
                "min_temp": daily_data["day"]["mintemp_c"],
                "description": daily_data["day"]["condition"]["text"],
                "icon": daily_data["day"]["condition"]["icon"],
            })

        return render_template("weather.html", current=weather_data, forecast=forecast_data)





@app.route("/flood", methods=["GET", "POST"])
def flood():
    if request.method == "POST":
        geocoding_url = "https://api.opencagedata.com/geocode/v1/json?q={}%2C{}&key=c78bc621f5d74ecbb3eb86bd62a68024"

        lat1 = float(request.form.get("latitude"))
        lon1 = float(request.form.get("longitude"))

        geocode_response = requests.get(geocoding_url.format(lat1, lon1)).json()

        state = geocode_response["results"][0]["components"]["state"].upper()
        district = geocode_response["results"][0]["components"]["district"]
        country = geocode_response["results"][0]["components"]["country"]

        if country == "Malaysia":
            flood_response = requests.get("https://api.data.gov.my/flood-warning").json()

            # capturing all data for the fetched state
            filtered_data = []
            for entry in flood_response:
                if entry["state"] == state:
                    filtered_data.append(entry)

            # capturing all coordinates of monitoring stations
            monitoring_stations = []
            for entry in filtered_data:
                monitoring_stations.append({
                    "latitude": float(entry["latitude"]),
                    "longitude": float(entry["longitude"])
                })


            # calculating nearest monitoring station
            min_distance = float('inf') # starting distance is infinite
            closest_location = None

            for coord in monitoring_stations:
                (lat2, lon2) = coord["latitude"], coord["longitude"]
                distance = haversine(lat1, lon1, lat2, lon2)

                if distance < min_distance:
                    min_distance = distance
                    closest_location = (lat2, lon2)


            # capturing data for nearest monitoring station
            display_data = []
            for entry in filtered_data:
                if (entry["latitude"], entry["longitude"]) == closest_location:
                    display_data.append(entry)


            for entry in display_data:
                rainfall = entry["rainfall_indicator"]
                if rainfall != None:
                    if rainfall == "NO_RAINFALL":
                        entry["rainfall_indicator"] = "NO RAINFALL"
                    elif rainfall == "ERROR":
                        entry["rainfall_indicator"] = "NO DATA"
                else:
                    print("Rainfall status: None")


            return render_template("flood.html", state=state, district=district, data=display_data)

        else:
            error_message = "Invalid Location"
            return render_template("flood.html", error_message=error_message)

    else:
        return render_template("flood.html")




@app.route("/satellite", methods=["GET"])
def satellite():
    return render_template("satellite.html")




@app.route("/earthquake", methods=["GET", "POST"])
def earthquake():
    if request.method == "POST":
        geocoding_url = "https://api.opencagedata.com/geocode/v1/json?q={}%2C{}&key=c78bc621f5d74ecbb3eb86bd62a68024"

        lat1 = float(request.form.get("latitude"))
        lon1 = float(request.form.get("longitude"))

        geocode_response = requests.get(geocoding_url.format(lat1, lon1)).json()

        state = geocode_response["results"][0]["components"]["state"]
        district = geocode_response["results"][0]["components"]["district"]
        country = geocode_response["results"][0]["components"]["country"]

        if country == "Malaysia":
            earthquake_response = requests.get("https://api.data.gov.my/weather/warning/earthquake").json()

            earthquake_data = []
            for entry in earthquake_response:
                earthquake_data.append(entry)

            # capturing all coordinates of earthquake
            earthquake_locations = []
            for entry in earthquake_data:
                earthquake_locations.append({
                    "latitude": float(entry["lat"]),
                    "longitude": float(entry["lon"])
                })


            # calculating nearest earthquake location
            min_distance = float('inf') # starting distance is infinite
            closest_location = None

            for coord in earthquake_locations:
                (lat2, lon2) = coord["latitude"], coord["longitude"]
                distance = haversine(lat1, lon1, lat2, lon2)

                if distance < min_distance:
                    min_distance = distance
                    closest_location = (lat2, lon2)


            # capturing data for nearest monitoring station
            display_data = []
            for entry in earthquake_data:
                if (entry["lat"], entry["lon"]) == closest_location:
                    display_data.append(entry)


            datetime_str = earthquake_data[0]["localdatetime"]
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
            date_only = datetime_obj.strftime("%Y-%m-%d")

            depth = round(earthquake_data[0]["depth"])

            return render_template("earthquake.html", state=state, district=district, data=display_data, distance=round(min_distance), date=date_only, depth=depth)

        else:
            error_message = "Invalid Location"
            return render_template("earthquake.html", error_message=error_message)

    else:
        return render_template("earthquake.html")
