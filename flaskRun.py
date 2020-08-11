import flask
from flask import Flask,request
import selenium
from selenium import webdriver
import backend
app = Flask(__name__)

ANKUR_WEBDRIVER = "/Users/ankuringale/Desktop/chromedriver"
MIHIR_WEBDRIVER = "/home/mihir/bin/chromedriver"

sample_object = {
	'link': '#',
	'name': 'Medicine',
	'price': 0
}

sample_data = [{
	'apollo': sample_object,
	'pharmeasy': sample_object,
	'netmeds': sample_object,
	'onemg': sample_object
}] * 5


@app.route('/')
def index(data = None):
	return flask.render_template('index.html', data=data)

@app.route('/handle_data', methods = ['POST'])
def handle_data():
	data, src = backend.compileData([request.form['type'], request.form['name']])
	searched_text = request.form['name']
	return flask.render_template('index.html', data=data, src=src, search=searched_text)

def getDriver():
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--incognito')
	options.add_argument('--headless')
	driver = webdriver.Chrome(MIHIR_WEBDRIVER, chrome_options=options)
	return driver

if __name__ == '__main__':
	app.debug=True
	app.run()    