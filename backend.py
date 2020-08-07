from flaskRun import getDriver

def f_1mg(medicine):
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

def f_pharmeasy(medicine):
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


def f_apollo(medicine):
	driver = getDriver()
	driver.get("https://www.apollopharmacy.in/tsearch?q="+medicine)
	try:
		unavailable = driver.find_element_by_class_name("no-products")
		return medicine + ' not found'
	except NoSuchElementException :
		pdt = driver.find_element_by_class_name("tagalys-product-tile")
		a = pdt.text.split('\n')
		return (a[0] + ' '+ a[1]).capitalize()
	# pass

def f_netmeds(medicine):
	driver = getDriver()
	URL = "https://www.netmeds.com/catalogsearch/result?q=" + medicine
	driver.get(URL)
	try:
		pdt = driver.find_element_by_class_name("drug_list")
		a = pdt.text.split('\n')[:5]
		return a[0] +' '+ a[2]
	except NoSuchElementException:
		return medicine + ' not found'
