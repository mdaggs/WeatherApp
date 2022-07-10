#Weather APP
import requests
from data import data
from config import apikey


class Weather:
	def __init__(self, apikey, lat, lon):
		self.apikey = apikey
		self.lat = lat
		self.lon = lon

	def HourlyForecast(self):

		url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely"

		querystring = {"lat":self.lat, "lon": self.lon}

		headers = {
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		return response.text


print(f"API Key is: {apikey}")
weather = Weather(apikey = apikey, lat = 36.153980, lon = -95.992775)
print(weather.HourlyForecast())