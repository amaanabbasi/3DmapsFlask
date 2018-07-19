# mapbox_access_token = 'PUT TOKEN HERE.
import flask
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__)


@app.route('/',methods=['GET','POST'])
def my_maps():

	mapbox_access_token = 'Your api key'
	
	return render_template('index.html', mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
	app.run(debug=True)
