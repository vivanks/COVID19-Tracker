# COVID19 Tracker

The COVID-19 tracker is a web application based on live tracking of COVID-19 stats all over the world.

It used this [API](https://rapidapi.com/spamakashrajtech/api/corona-virus-world-and-india-data) to extract the number of cases confirmed, recovered and  number of deaths for each country in the world and for each state of India. 

The website has a feature of live update and displays the most recent stats.

It also uses plotly library from Python to visualise the rise in number of cases with each passing day.

The COVID19 tracker is hosted on heroku and can be accessed [here](http://vivanks-covid19.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

For running the project you will be needing Python 3 and Flask installed in your system with an active internet connection for rest-api to work.

```
python app.py
```

## Installing

Create new env using

```
conda create -n my_flask_env
source activate my_flask_env 
```
Install all the requirements using:

```
pip install -r requirements.txt
```

## Deployment

You can deploy using heroku by following [this](https://devcenter.heroku.com/categories/python-support) 

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Rapid API](https://rapidapi.com/spamakashrajtech/api/corona-virus-world-and-india-data) - Rest API manager used to get data.

## Contributing

COVID19-Tracker is very seriously a work in progress. Any help, interaction, and input is welcome and encouraged. Feel free to make any contributions, whether it be typos, documentation, new features, bug fixes, etc. Suggest features and functionality, open PRs and issues, or tackle any of the open issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [ spamakashrajtech ](https://rapidapi.com/user/spamakashrajtech) for creating API.
* [ SB Admin ](https://startbootstrap.com/themes/sb-admin-2/) for admin dashboard template.
* [ Plotly ](https://plotly.com/) for interactive graphs
