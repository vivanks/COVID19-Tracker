import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time
import json
import plotly
from flask import jsonify

class Covid19Data:

	'''
	Class for connecting and getting data from RapidAPI's Corona virus World and India data

	Documentation for usage of this API can be found here : https://rapidapi.com/spamakashrajtech/api/corona-virus-world-and-india-data
	
	'''
	def __init__(self):

		# Secret keys
		self.headers = {
				    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
				    'x-rapidapi-key': "95f7dcf64bmshae89e3e043a70c4p134474jsn00b8704e368c"
				  }

		# URL to get the data of cases of COVID'19 in whole world country wise.
		self.world_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

		#Calling API with world_url and storing the result in World Response.
		self.world_response = requests.request("GET", self.world_url, headers=self.headers).json()

		# Free API limits 1 call per second so waiting for 1 second to pass
		time.sleep(1)

		# URL for getting data of cases of COVID'19 in India statewise
		self.india_url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

		#Calling API with india_url and storing the result in india_response.
		self.india_response = requests.request("GET", self.india_url, headers=self.headers).json()

		# Free API limits 1 call per second so waiting for 1 second to pass
		time.sleep(1)

		self.india_timeline = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india_timeline"

		self.itr = requests.request("GET", self.india_timeline, headers=self.headers).json()

	def getWorld(self):
		'''
		Desc : Getter for getting world_repsonse in JSON format
		input : Self Object
		output : JSON of response of cases of COVID'19 in whole world country wise.
		'''
		return self.world_response

	def getIndia(self):
		'''
		Desc : Getter for getting india_response in JSON format
		input : Self Object
		output : JSON of response of cases of COVID'19 in India statewise
		'''
		return self.india_response

	def getWorldTotal(self):
		'''
		Desc : Getter for getting world_repsonse in JSON format
		input : Self Object
		output : JSON of response of cases of COVID'19 summed up of whole world together
		'''
		return self.world_response

	def create_plot(self):
		'''
		Desc : A function for returning total statistics of active cases, recovered cases, deceased cases
		input : self class object
		output: labels -> String Array -> Label for different types of cases
				values_india -> Int Array -> [india_active_cases,india_deaths_cases,india_recovered_cases]
				values_world -> Int Array -> [world_active_cases,world_deaths_cases,world_recovered_cases]
		'''
		country = "India"
		country_stats = {}
		for i in self.world_response['countries_stat']:
			if i['country_name'] == country:
				country_stats=i
		
		# Extracting the total active cases of COVID'19 in India from the API data 
		india_active = int(country_stats['cases'].replace(',', ''))-int(country_stats['deaths'].replace(',', ''))-int(country_stats['total_recovered'].replace(',', ''))

		# Extracting the total descease due to COVID'19 in India from the API data
		india_deaths = int(country_stats['deaths'].replace(',',''))

		# Extracting the total number of recovered cases of COVID'19 in India
		india_recovered = int(country_stats['total_recovered'].replace(',',''))

		# Extracting the total active cases of COVID'19 in World from the API data
		world_active = int(self.world_response['world_total']['total_cases'].replace(',','')) -  int(self.world_response['world_total']['total_deaths'].replace(',',''))- int(self.world_response['world_total']['total_recovered'].replace(',',''))

		# Extracting the total descease due to COVID'19 in whole World from the API data
		world_deaths = int(self.world_response['world_total']['total_deaths'].replace(',',''))

		# Extracting the total number of recovered cases of COVID'19 in World
		world_recovered = int(self.world_response['world_total']['total_recovered'].replace(',',''))

		#Storing all the data in an array
		labels = ['Active','Death','Recovered']

		values_india = [india_active,india_deaths,india_recovered]
		values_world = [world_active,world_deaths,world_recovered]


		return labels,values_india,values_world

	def getTimline(self):

		'''
		Desc: A function to extract and return an array of history of case of COVID'19 in India from January 29th
		input: Self class object
		output: date_json -> array of all the dates
				daily_confirmed_json -> array containing number of daily confirmed cases according to date_json array,
				daily_deceased_json -> array containing number of daily deceased cases according to date_json array,
				daily_recovered_json -> array containing number of daily recovered cases according to date_json array,
				total_confirmed_json -> array containing number of confirmed cases till date according to date_json array.
				total_deceased_json -> array containing number of deceased cases till date according to date_json array.
				total_recovered_json -> array containing number of recovered cases till date according to date_json array.
		'''
		
		self.df_hist = pd.DataFrame.from_records(self.itr)

		date_json = self.df_hist['date'].tolist()
		

		daily_confirmed_json = self.df_hist['dailyconfirmed'].apply(pd.to_numeric).tolist()
		

		daily_deceased_json = self.df_hist['dailydeceased'].apply(pd.to_numeric).tolist()

		daily_recovered_json = self.df_hist['dailyrecovered'].apply(pd.to_numeric).tolist()

		total_confirmed_json = self.df_hist['totalconfirmed'].apply(pd.to_numeric).tolist()
		

		total_deceased_json = self.df_hist['totaldeceased'].apply(pd.to_numeric).tolist()

		total_recovered_json = self.df_hist['totalrecovered'].apply(pd.to_numeric).tolist()
		

		return date_json,daily_confirmed_json,daily_deceased_json,daily_recovered_json,total_confirmed_json,total_deceased_json,total_recovered_json



