from tracker import app

import json, plotly
from flask import render_template,url_for
from covid19api import Covid19Data

from datetime import datetime
from pytz import timezone
format = "%Y-%m-%d %H:%M:%S"
format1 = "%H:%M %p /\\ %d-%m-%Y"
from dateutil.tz import *


@app.route('/')
@app.route('/index')
def index():
	cd = Covid19Data()

	world_data = cd.getWorldTotal()

	# Current time in UTC
	time = world_data['statistic_taken_at']
	time = datetime.strptime(time,format)
	time = time.replace(tzinfo = tzutc())
	now_asia = time.astimezone(timezone('Asia/Kolkata'))
	

	wtc = world_data['world_total']['total_cases']
	wnc = world_data['world_total']['new_cases']
	wdc = world_data['world_total']['total_deaths']

	
	
	country_stats = {}
	for i in world_data['countries_stat']:
		if i['country_name'] == 'India':
			country_stats=i

	labels,values_india,values_world = cd.create_plot()


	
	
	return render_template('index.html',
							world_data =  world_data['world_total'],
							india_data = country_stats,
							world_track = world_data['countries_stat'],
							values_india = json.dumps(values_india),
							values_world = json.dumps(values_world),
							time = now_asia.strftime(format1)
												)

@app.route('/india')
def india():

	cd = Covid19Data()

	india_data = cd.getIndia()

	statewise = india_data['state_wise']


	return render_template('tables.html',statewise=statewise)


