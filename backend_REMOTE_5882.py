from flaskRun import getDriver
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