import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time


class Covid19Data:
	headers = {
				    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
				    'x-rapidapi-key': "95f7dcf64bmshae89e3e043a70c4p134474jsn00b8704e368c"
				  }

	world_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
	

	def __init__(self):
		

		self.world_response = requests.request("GET",self.world_url, headers=self.headers).json()

		self.world_total = world_response['world_total']

		time.sleep(1)

		india_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

		self.india_response = requests.request("GET", india_url, headers=headers).json()


	def getWorld(self):
		return self.world_response

	def getIndia(self):
		return self.india_response

	def getWorldTotal(self):
		return self.world_total





