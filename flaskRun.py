import flask
from flask import Flask,request
import selenium
from selenium import webdriver
import backend
from backend import *
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)

driver = None
ANKUR_WEBDRIVER = "/Users/ankuringale/Desktop/chromedriver"
MIHIR_WEBDRIVER = "/home/mihir/bin/chromedriver"

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

def getDriver():
	global driver
	return driver


if __name__ == '__main__':
	app.debug=True
	app.run()