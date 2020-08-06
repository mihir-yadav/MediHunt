import flask
from flask import Flask,request
import selenium
from selenium import webdriver
app = Flask(__name__)

driver = None
ANKUR_WEBDRIVER = "/Users/ankuringale/Desktop/chromedriver"
MIHIR_WEBDRIVER = "/home/mihir/bin/chromedriver"

@app.route('/')
def index():
	global driver
	if not driver:
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--incognito')
		options.add_argument('--headless')
		driver = webdriver.Chrome(ANKUR_WEBDRIVER, chrome_options=options)
	return flask.render_template('index.html')

@app.route('/handle_data', methods = ['POST'])
def handle_data():
	projectpath = request.form['name']
	driver.get('https://www.google.com/')
	driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(projectpath)
	driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').submit()
	print(driver.current_url)
	return flask.render_template('index.html')

def getDriver():
	global driver
	return driver

if __name__ == '__main__':
	app.debug=True
	app.run()    