import flask
from flask import Flask,request
import selenium
from selenium import webdriver
import backend
<<<<<<< HEAD
from backend import *
from selenium.common.exceptions import NoSuchElementException

=======
>>>>>>> fbbb945bb9f512bbc16f466695688c8996c630dd
app = Flask(__name__)

driver = None
ANKUR_WEBDRIVER = "/Users/ankuringale/Desktop/chromedriver"
MIHIR_WEBDRIVER = "/home/mihir/bin/chromedriver"

<<<<<<< HEAD
def find_apollo(medicine):
	global driver
	driver.get("https://www.apollopharmacy.in")
	driver.find_element_by_xpath('//*[@id="search"]').send_keys(medicine)
	driver.find_element_by_xpath('//*[@id="search"]').submit()
	# print(driver.current_url)
	for i in range(5):
		pdt = driver.find_element_by_xpath('//*[@id="tagalys-namespace"]/div/div[2]/div[2]/div['+str(i+1)+']')
		a = pdt.text.split('\n')
		for x in a :
			print(x)
		link = pdt.get_attribute('href')
		print(link)

# //*[@id="tagalys-namespace"]/div/div[2]/div[2]/div[1]/a
# //*[@id="tagalys-namespace"]/div/div[2]/div[2]/div[1]
# //*[@id="tagalys-namespace"]/div/div[2]/div[2]/div[2]
# 	# driver.get("https://www.apollopharmacy.in/tsearch?q="+medicine)
	# try:
	# 	unavailable = driver.find_element_by_class_name("no-products")
	# 	return medicine + ' not found'
	# except NoSuchElementException :
	# 	pdt = driver.find_element_by_class_name("tagalys-product-tile")
	# 	a = pdt.text.split('\n')
	# 	return (a[0] + ' '+ a[1]).capitalize()



@app.route('/')
def index():
	global driver
	if not driver:
		options = webdriver.ChromeOptions()
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--incognito')
		options.add_argument('--headless')
		driver = webdriver.Chrome(MIHIR_WEBDRIVER, chrome_options=options)
	return flask.render_template('index.html')

@app.route('/handle_data', methods = ['POST'])
def handle_data():
	global driver

	projectpath = request.form.getlist('name')
	medicine = projectpath[1] 
	# driver.get("https://www.apollopharmacy.in/tsearch?q="+medicine)
	# + '%20' + projectpath[1]
	print(medicine)
	# desc = f_netmeds(medicine)
	desc = find_apollo(medicine)
	print(desc)
	# driver.get('https://www.google.com/')
	# driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(projectpath)
	# driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').submit()
	# print(driver.current_url)
	return flask.render_template('index.html')
=======
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
	data = backend.compileData([request.form['type'], request.form['name']])
	return flask.render_template('index.html', data=data)
>>>>>>> fbbb945bb9f512bbc16f466695688c8996c630dd

def getDriver():
	global driver
	if not driver:
		initDriver()
	assert driver is not None
	return driver

<<<<<<< HEAD
=======
def initDriver():
	global driver
	options = webdriver.ChromeOptions()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--incognito')
	options.add_argument('--headless')
	driver = webdriver.Chrome(ANKUR_WEBDRIVER, chrome_options=options)
>>>>>>> fbbb945bb9f512bbc16f466695688c8996c630dd

if __name__ == '__main__':
	app.debug=True
	app.run()