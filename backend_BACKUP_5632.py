from flaskRun import getDriver
<<<<<<< HEAD

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
=======
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

def f_1mg(medicine):
    data = [
        {
            'link': '#',
            'name': '',
            'price': ''
        }
    ] * 5
    return data

def f_pharmeasy(medicine):
    data = [
        {
            'link': '#',
            'name': '',
            'price': ''
        }
    ] * 5
    return data

def f_apollo(medicine):
    URL = "https://www.apollopharmacy.in/"
    driver = getDriver()
    driver.get(URL)
    delay = 4

    data = [
        {
            'link': '#',
            'name': '',
            'price': ''
        }
    ] * 5

    try:
        driver.find_element_by_id('search').send_keys(' '.join(medicine))
        driver.find_element_by_id('search').send_keys(Keys.ENTER)

        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'header-results-and-footer')
            ))

            boxes = driver.find_elements_by_class_name('product-link')

            for i, box in enumerate(boxes):
                data_obj = {
                    'link': '#',
                    'name': '',
                    'price': ''
                }
                data_obj['link'] = box.get_attribute('href')
                data_obj['name'] = box.find_element_by_class_name('product-name').text
                data_obj['price'] = box.find_element_by_class_name('product-sale-price').text
                data[i] = data_obj
        except:
            pass
    except:
        pass
    
    return data

def f_netmeds(medicine):
    URL = "https://www.netmeds.com/"
    driver = getDriver()
    driver.get(URL)
    delay = 4

    data = [
        {
            'link': '#',
            'name': '',
            'price': ''
        }
    ] * 5

    try:
        driver.find_element_by_id('search').send_keys(' '.join(medicine))
        driver.find_element_by_id('search').send_keys(Keys.ENTER)

        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'sear-name')
            ))

            boxes = driver.find_elements_by_class_name('drug_list')

            for i, box in enumerate(boxes):
                data_obj = {
                    'link': '#',
                    'name': '',
                    'price': ''
                }
                obj = box.find_element_by_class_name('drug_c').find_element_by_tag_name('a')
                data_obj['link'] = obj.get_attribute('href')
                data_obj['name'] = obj.find_element_by_class_name('info').text
                data_obj['price'] = box.find_element_by_class_name('final-price').text
                data[i] = data_obj
        except:
            pass
    except:
        pass
    
    print(data)
    return data

def compileData(medicine):
    apollo = f_apollo(medicine)
    pharmeasy = f_pharmeasy(medicine)
    netmeds = f_netmeds(medicine)
    onemg = f_1mg(medicine)

    data = [0] * 5
    for i in range(5):
        data[i] = {
            'apollo': apollo[i],
            'pharmeasy': pharmeasy[i],
            'netmeds': netmeds[i],
            'onemg': onemg[i]
        }
    return data
>>>>>>> fbbb945bb9f512bbc16f466695688c8996c630dd
