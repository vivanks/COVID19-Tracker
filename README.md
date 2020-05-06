# COVID19 Tracker

A COVID19 cases tracker of World and India.

The COVID19 tracker is hosted on heroku and can be accessed [here](http://vivanks-covid19.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For running the project you will be needing Python 3 and Flask installed in your system with an active internet connection for rest-api to work.

```
python app.py
```

### Installing

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


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* [ spamakashrajtech ](https://rapidapi.com/user/spamakashrajtech) for creating API.
* [ SB Admin ](https://startbootstrap.com/themes/sb-admin-2/) for admin dashboard template.
* [ Plotly ](https://plotly.com/) for interactive graphs
