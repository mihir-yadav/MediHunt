from flaskRun import getDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from threading import Thread
from multiprocessing import Process, Pool
import datetime
from datetime import datetime
 
apollo, pharmeasy, netmeds, onemg, src = [None] * 5
driver_apollo, driver_pharmeasy, driver_netmeds, driver_onemg, driver_src = [None] * 5

def get_img_src(medicine_with_type):
	global src, driver_src
	driver = driver_src
	medicine = ' '.join(medicine_with_type)
	driver.get('https://images.google.com')
	driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys(medicine)
	driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input').send_keys(Keys.ENTER)
	src = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').get_attribute('src')
	driver_src.quit()
	return src

def f_1mg(medicine):

	start_time_1mg = datetime.now()
	global onemg, driver_onemg

	driver = driver_onemg
	data = [
		{
			'link': '#',
			'name': '',
			'price': ''
		}
	] * 5
	URL = "https://www.1mg.com/search/all?name=" + '%20'.join(medicine)
	driver.get(URL)
	delay = 4
	driver_time_1mg= datetime.now()
	print(driver.current_url)
	# return data
	try:
		# # driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/input')
		# driver.find_element_by_class_name('jss34 _9Rsw_ undefined _2Saml')		
		# driver.send_keys(' '.join(medicine))
		# driver.send_keys(Keys.ENTER)
		# driver.
		# print('searched\n')
		# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div
		# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[2]
		
		try:
			WebDriverWait(driver, delay).until(EC.presence_of_element_located(
				(By.CLASS_NAME, 'row.style__grid-container___3OfcL')
			))
			# try :
				# driver.find_element_by_class_name('style__horizontal-card___1Zwmt')
				# print('found1\n')
			boxes = driver.find_elements_by_class_name('style__horizontal-card___1Zwmt')
			if len(boxes) > 0: 
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
					if data_obj['price'][0:3] == 'MRP' :
						data_obj['price'] = data_obj['price'][3:]
					data[i] = data_obj
					data[i] = data_obj
					# print(i)
			# except:
			else :
				# try:					
				boxes = driver.find_elements_by_class_name('style__product-box___3oEU6')
				if len(boxes) > 0 :
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
						price = box.find_element_by_class_name('style__price-tag___KzOkY').text
						price = str(price)
						data_obj['price'] = price.replace('MRP', '')
						# except : 
						# 	data_obj['price'] = box.find_element_by_class_name('nFRb7').text 
						if data_obj['price'][0:3] == 'MRP' :
							data_obj['price'] = data_obj['price'][3:]
						data[i] = data_obj
						# print(i)
				# except:
				else :
					pass
		except:
			pass
	except:
		pass
	# if(data[])
	end_time_1mg = datetime.now()
	print('1mg',end=" ")
	print(start_time_1mg.time(),driver_time_1mg ,end_time_1mg.time())

	onemg = data
	driver.quit()
	return onemg
	# return data

def f_pharmeasy(medicine):
	start_time_pharmeasy = datetime.now()
	global pharmeasy, driver_pharmeasy

	driver = driver_pharmeasy
	data = [
		{
			'link': '#',
			'name': '',
			'price': ''
		}
	] * 5
	URL = "https://pharmeasy.in/search/all?name=" + '+'.join(medicine)
	driver.get(URL)
	delay = 4
	driver_time_pharmeasy = datetime.now()
	print(driver.current_url)
	# return data
	# try:
		# # driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/input')
		# driver.find_element_by_class_name('jss34 _9Rsw_ undefined _2Saml')		
		# driver.send_keys(' '.join(medicine))
		# driver.send_keys(Keys.ENTER)
		# driver.
	# print('searched\n')
	# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div
	# //*[@id="content"]/div/div[3]/div/div/div[1]/div[1]/div/div[2]
	
	try:
		WebDriverWait(driver, delay).until(EC.presence_of_element_located(
			(By.CLASS_NAME, '_3zq4I')
		))
		# print('found\n')
		boxes = driver.find_elements_by_class_name('_1jald')
		if len(boxes) > 0 :
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
				# print(i)
		else :
			pass
	except:
		pass
	# except:
	# 	pass

	end_time_pharmeasy = datetime.now()
	print('Pharmeasy',end=" ")
	print(start_time_pharmeasy.time(),driver_time_pharmeasy, end_time_pharmeasy.time())
	pharmeasy = data
	driver.quit()
	return pharmeasy
	# return data

def f_apollo(medicine):
	start_time_apollo = datetime.now()
	global apollo, driver_apollo

	driver = driver_apollo
	# pass
	URL = "https://www.apollopharmacy.in/"
	driver.get(URL)
	delay = 4
	driver_time_apollo = datetime.now()
	print(driver.current_url)

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

	end_time_apollo = datetime.now()
	print('Apollo',end=" ")
	print(start_time_apollo.time(),driver_time_apollo ,end_time_apollo.time())
	apollo = data
	driver.quit()
	return apollo
	# return data

def f_netmeds(medicine):
	start_time_netmeds = datetime.now()
	global netmeds, driver_netmeds

	driver = driver_netmeds
	URL = "https://www.netmeds.com/"
	driver.get(URL)
	delay = 4
	driver_time_netmeds= datetime.now()
	print(driver.current_url)

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
	
	end_time_netmeds = datetime.now()
	print('Netmeds',end=" ")
	print(start_time_netmeds.time(),driver_time_netmeds ,end_time_netmeds.time())
	# print(data)
	netmeds = data
	driver.quit()
	return netmeds
	# return data

def compileData(medicine):
	global apollo, pharmeasy, netmeds, onemg, src
	global driver_src, driver_netmeds, driver_pharmeasy, driver_onemg, driver_apollo

	driver_src = getDriver()
	driver_netmeds = getDriver()
	driver_pharmeasy = getDriver()
	driver_onemg = getDriver()
	driver_apollo = getDriver()

	# print("Start time: ")
	# print(datetime.datetime.now().time())
	start_time = datetime.now()

	# thread_apollo = Thread(target = f_apollo,args = (medicine,))
	# thread_pharmeasy = Thread(target = f_pharmeasy,args = (medicine,))
	# thread_netmeds = Thread(target = f_netmeds,args = (medicine,))
	# thread_onemg = Thread(target = f_1mg,args = (medicine,))
	# thread_src = Thread(target = get_img_src, args = (' '.join(medicine),))
	
	# thread_apollo = Process(target = f_apollo,args = (medicine,))
	# thread_pharmeasy = Process(target = f_pharmeasy,args = (medicine,))
	# thread_netmeds = Process(target = f_netmeds,args = (medicine,))
	# thread_onemg = Process(target = f_1mg,args = (medicine,))
	# thread_src = Process(target = get_img_src, args = (' '.join(medicine),))

	pool = Pool(4)
	thread_onemg = pool.apply_async(f_1mg, (medicine, ))
	thread_apollo = pool.apply_async(f_apollo, (medicine, ))
	thread_pharmeasy = pool.apply_async(f_pharmeasy, (medicine, ))
	thread_netmeds = pool.apply_async(f_netmeds, (medicine, ))
	# thread_src = pool.apply_async(get_img_src, (medicine, ))

	pool.close()
	pool.join()

	apollo = thread_apollo.get(10)
	pharmeasy = thread_pharmeasy.get(10)
	onemg = thread_onemg.get(10)
	netmeds = thread_netmeds.get(10)

	src = get_img_src(medicine)
	# src = thread_src.get(10)
	
	# thread_apollo.start()
	# thread_pharmeasy.start()
	# thread_netmeds.start()
	# thread_onemg.start()
	# thread_src.start()

	# thread_apollo.join()
	# thread_pharmeasy.join()
	# thread_netmeds.join()
	# thread_onemg.join()
	# thread_src.join()


	# f_apollo(medicine)
	# f_pharmeasy(medicine)
	# f_netmeds(medicine)
	# f_1mg(medicine)
	# print("End time: ")
	# print(datetime.datetime.now().time())
	end_time = datetime.now()
	print('time taken: ',end= " ")
	print(end_time - start_time)

	data = [0] * 5
	for i in range(5):
		data[i] = {
			'apollo': apollo[i],
			'pharmeasy': pharmeasy[i],
			'netmeds': netmeds[i],
			'onemg': onemg[i]
		}
	return data, src