from flaskRun import getDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


def get_img_src(medicine):
	driver= getDriver()
	driver.get('https://images.google.com');
	driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys(' '.join(medicine))
	print(' '.join(medicine))
	driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys(Keys.ENTER)
	src = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute('src')
	return src


def f_1mg(medicine):
	data = [
		{
			'link': '#',
			'name': '',
			'price': ''
		}
	] * 5
	URL = "https://www.1mg.com/search/all?name=" + '%20'.join(medicine)
	driver = getDriver()
	driver.get(URL)
	delay = 4
	# return data
	try:
		# # driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/input')
		# driver.find_element_by_class_name('jss34 _9Rsw_ undefined _2Saml')		
		# driver.send_keys(' '.join(medicine))
		# driver.send_keys(Keys.ENTER)
		# driver.
		print('searched\n')
		# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div
		# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[2]
		print(driver.current_url)
		try:
			WebDriverWait(driver, delay).until(EC.presence_of_element_located(
				(By.CLASS_NAME, 'row.style__grid-container___3OfcL')
			))
			try :
				driver.find_element_by_class_name('style__horizontal-card___1Zwmt')
				print('found1\n')
				boxes = driver.find_elements_by_class_name('style__horizontal-card___1Zwmt')
				print(len(boxes))
				for i, box in enumerate(boxes):
					data_obj = {
						'link': '#',
						'name': '',
						'price': ''
					}
					data_obj['link'] = box.find_element_by_tag_name('a').get_attribute('href')
					# data_obj['name'] = box.find_element_by_class_name('style__pro-title___3zxNC').text 
					data_obj['name'] = box.find_element_by_class_name('style__product-description___1vPQe').text
					# 
					# +'\n'+ box.find_element_by_class_name('_36aef').text
					# try :
					data_obj['price'] = box.find_element_by_class_name('style__price-tag___B2csA').text
					# except : 
					# 	data_obj['price'] = box.find_element_by_class_name('nFRb7').text 
			
					data[i] = data_obj
					print(i)
			except:
				try:
					driver.find_element_by_class_name('style__product-box___3oEU6')
					print('found2\n')
					boxes = driver.find_elements_by_class_name('style__product-box___3oEU6')
					print(len(boxes))
					for i, box in enumerate(boxes):
						data_obj = {
							'link': '#',
							'name': '',
							'price': ''
						}
						data_obj['link'] = box.find_element_by_tag_name('a').get_attribute('href')
						# data_obj['name'] = box.find_element_by_class_name('style__pro-title___3zxNC').text 
						data_obj['name'] = box.find_element_by_class_name('style__product-description___zY35s').text
						# 
						# +'\n'+ box.find_element_by_class_name('_36aef').text
						# try :
						data_obj['price'] = box.find_element_by_class_name('style__price-tag___KzOkY').text
						# except : 
						# 	data_obj['price'] = box.find_element_by_class_name('nFRb7').text 
				
						data[i] = data_obj
						print(i)
				except:
					pass
		except:
			pass
	except:
		pass
	return data


def f_pharmeasy(medicine):
	data = [
		{
			'link': '#',
			'name': '',
			'price': ''
		}
	] * 5
	URL = "https://pharmeasy.in/search/all?name=" + '+'.join(medicine)
	driver = getDriver()
	driver.get(URL)
	delay = 4
	# return data
	try:
		# # driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/input')
		# driver.find_element_by_class_name('jss34 _9Rsw_ undefined _2Saml')		
		# driver.send_keys(' '.join(medicine))
		# driver.send_keys(Keys.ENTER)
		# driver.
		print('searched\n')
		# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div
		# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[2]
		print(driver.current_url)
		try:
			WebDriverWait(driver, delay).until(EC.presence_of_element_located(
				(By.CLASS_NAME, '_3zq4I')
			))
			print('found\n')
			boxes = driver.find_elements_by_class_name('_1jald')
			print(len(boxes))
			for i, box in enumerate(boxes):
				data_obj = {
					'link': '#',
					'name': '',
					'price': ''
				}
				data_obj['link'] = box.find_element_by_class_name('_3o0NT._1NxW8').get_attribute('href')
				data_obj['name'] = box.find_element_by_class_name('ooufh').text 
				# +'\n'+ box.find_element_by_class_name('_36aef').text
				try :
					data_obj['price'] = box.find_element_by_class_name('_1_yM9').text[:-1]
				except : 
					data_obj['price'] = box.find_element_by_class_name('nFRb7').text 
		
				data[i] = data_obj
				print(i)

		except:
			pass
	except:
		pass
	return data

def f_apollo(medicine):
	pass
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
	# return data
	try:
		driver.find_element_by_id('search').send_keys(' '.join(medicine))
		driver.find_element_by_id('search').send_keys(Keys.ENTER)

		try:
			WebDriverWait(driver, delay).until(EC.presence_of_element_located(
				(By.CLASS_NAME, 'header-results-and-footer')
			))

			boxes = driver.find_elements_by_class_name('product-link')
			# print(len(boxes))
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
				# print(i)

		except:
			pass
	except:
		pass
	
	return data

def f_netmeds(medicine):
	pass
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
	# return data
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