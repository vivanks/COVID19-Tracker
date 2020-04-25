import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import json
import plotly

class Covid19Data:

	def __init__(self):
		headers = {
				    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
				    'x-rapidapi-key': "95f7dcf64bmshae89e3e043a70c4p134474jsn00b8704e368c"
				  }

		world_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

		self.world_response = requests.request("GET", world_url, headers=headers).json()

		time.sleep(1)

		india_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

		self.india_response = requests.request("GET", india_url, headers=headers).json()


	def getWorld(self):
		return self.world_response

	def getIndia(self):
		return self.india_response

	def getWorldTotal(self):
		return self.world_response

	def create_plot(self):

		country = "India"
		country_stats = {}
		for i in self.world_response['countries_stat']:
			if i['country_name'] == country:
				country_stats=i
		india_active = int(country_stats['cases'].replace(',', ''))-int(country_stats['deaths'].replace(',', ''))-int(country_stats['total_recovered'].replace(',', ''))

		india_deaths = int(country_stats['deaths'].replace(',',''))

		india_recovered = int(country_stats['total_recovered'].replace(',',''))

		world_active = int(self.world_response['world_total']['total_cases'].replace(',','')) -  int(self.world_response['world_total']['total_deaths'].replace(',',''))- int(self.world_response['world_total']['total_recovered'].replace(',',''))

		world_deaths = int(self.world_response['world_total']['total_deaths'].replace(',',''))

		world_recovered = int(self.world_response['world_total']['total_recovered'].replace(',',''))

		labels = ['Active','Death','Recovered']

		values_india = [india_active,india_deaths,india_recovered]
		values_world = [world_active,world_deaths,world_recovered]


		return labels,values_india,values_world



