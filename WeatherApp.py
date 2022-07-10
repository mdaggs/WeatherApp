#Weather APP
import requests
from data import data
from config import apikey, lat, lon


class Weather:
	def __init__(self, apikey, lat, lon):
		self.apikey = apikey
		self.lat = lat
		self.lon = lon

	def minutelyForecase(self):

		url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely"

		querystring = {"lat":self.lat, "lon": self.lon}

		headers = {
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		return response.text

	def hourlyForecast(self):

		url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly"

		querystring = {"lat":self.lat, "lon": self.lon}

		headers = {
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		return response.text

	def dailyForecast(self):

		url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"

		querystring = {"lat":self.lat, "lon": self.lon}

		headers = {
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		return response.text

	def threeHourlyForecast(self):

		url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

		querystring = {"lat":self.lat, "lon": self.lon}

		headers = {
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		return response.text

	def currentForecast(self):

		url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

		querystring = {"lat":self.lat, "lon": self.lon}

		headers = {
			"X-RapidAPI-Key": apikey,
			"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		return response.text


print(f"API Key is: {apikey}")
weather = Weather(apikey = apikey, lat = lat, lon = lon)
print(weather.currentForecast())



