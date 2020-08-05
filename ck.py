import flask
import requests
from bs4 import BeautifulSoup

def find_cost_1mg(medicine):
    URL = "https://www.1mg.com/search/all?name="+medicine
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,'html.parser')
#     print(soup.prettify())
    name = ""
    cost = ""
    name_table = soup.find('div',attrs = {'class':'style__product-description___1vPQe'})
    if(name_table):
        for row in name_table:
            name += row.text
            name += ','
        name = name[:-1]
        cost_table = soup.find('div',attrs = {'class':'style__price-tag___B2csA'})

        for row in cost_table:
            cost += row.string

        return name + ": " + cost
    else :
        return medicine + ' not found'
    
def find_cost_pharmeasy(medicine):
    URL = "https://pharmeasy.in/search/all?name=" + medicine
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,'html.parser')
    # print(soup.prettify())
    name = ""
    cost = ""
    desc = ""
    name_table = soup.find('h1',attrs = {'class':'ooufh'})
    if(name_table):
        for row in name_table:
            name = row.string
        name += ','    
        desc_table = soup.find('div',attrs = {'class':'_36aef'})
        if(desc_table):
            for row in desc_table:
                desc = row.string
            desc += ':'
            cost_table = soup.find('div',attrs = {'class':'_1_yM9'})
            for row in cost_table:
                cost +=  str(row.string)
            if cost[-1]=='*' :
                cost = cost[:-1]
            return name + desc + cost
        return medicine + ' not found'
    return medicine + ' not found'

import selenium
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/home/mihir/bin/chromedriver", chrome_options=options)

from selenium.common.exceptions import NoSuchElementException

def find_cost_apollo(medicine):
    driver.get("https://www.apollopharmacy.in/tsearch?q="+medicine)
    try:
        unavailable = driver.find_element_by_class_name("no-products")
        return medicine + ' not found'
    except NoSuchElementException :
        pdt = driver.find_element_by_class_name("tagalys-product-tile")
        a = pdt.text.split('\n')
        return (a[0] + ' '+ a[1]).capitalize()

def find_cost_netmeds(medicine):
    URL = "https://www.netmeds.com/catalogsearch/result?q=" + medicine
    driver.get(URL)
    try:
        pdt = driver.find_element_by_class_name("drug_list")
        a = pdt.text.split('\n')[:5]
        return a[0] + a[2]
    except NoSuchElementException:
        return medicine + ' not found'


from flask import Flask,request
app = Flask(__name__)




@app.route('/')
def index():
	return flask.render_template('index.html')

@app.route('/handle_data',methods = ['POST'])
def handle_data():
	projectpath = request.form.getlist('po')
	medicine = ""
	projectpath = projectpath[::-1]
	for x in projectpath :
		print(x)
		medicine += x
		medicine += ' '
	print (medicine)	
	costs = ""
	costs += find_cost_1mg(medicine)
	costs += '		'
	costs += find_cost_pharmeasy(medicine)
	costs += '		'
	costs += find_cost_apollo(medicine)
	costs += '		'
	costs += find_cost_netmeds(medicine)
	return costs

if __name__ == '__main__':
	app.debug=True
	app.run()    