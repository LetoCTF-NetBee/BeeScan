import requests
import json
from bs4 import BeautifulSoup
import whois
import time
from datetime import datetime
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


creation = ['Creation Date', 'created']


def scanDatabaseOpenphish(domain):
<<<<<<< HEAD
    file = open('openphish.txt', 'r')
    table = file.readlines()
    for i in table:
        if domain == i:
            return False, "Found in database"
    return True, "Not found in database"


=======
	file = open('openphish.txt', 'r')
	table = file.readlines()
	for i in table:
		if domain == i:
			return False, "Found in database"
	return True, "Not found in database"
>>>>>>> 20058ab4d24d2a1a1689c0dda3cbd299fc6cc018
def checkSSL(domain):
	try:
		requests.get('https://' + domain)
		return True, 'SSL redy'
	except:
		try:
			requests.get('http://' + domain)
			return False, 'SSL not found'
		except:
			return False, 'Site not found'


def returnDateCreationShopify(domain):
	try:
		url = 'https://www.shopify.com/tools/whois/search?query='
		request = requests.get(url + domain)
		soup = BeautifulSoup(request.text)
		result = soup.find('pre', {'class': 'whois-record'})
		for item in creation:
			if item in result.text:
				return result.text[result.text.find(item) + len(item) + 1: result.text.find('Z', result.text.find(item)) + 1], 'OK'
	except Exception as e:
		return datetime.now(), str(e)


def checkValidDate(domain, period):
	date, err = returnDateCreationShopify(domain)
	if err != 'OK':
		return False, err
	now = datetime.now()
	date = date.replace('T', ' ').replace('Z', ' ').strip()
	delta = now - datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
	if abs(delta.days) > period:
		return True, abs(delta.days - period)
	else:
		return False, abs(delta.days - period)


def testRedirection(url):
<<<<<<< HEAD
    driver = webdriver.Chrome('chromedriver.exe')
    ssl, _ = checkSSL(url)
    try:
        if ssl:
            url = 'https://' + url + '/'
        else:
            url = 'http://' + url + '/'
        driver.get(url)
        if driver.current_url != url:
            return False, driver.current_url
    except Exception as e:
        return False, 'error: ' + str(e)
    finally:
        driver.close()

=======
	driver = webdriver.Chrome('chromedriver.exe')
	ssl, _ = checkSSL(url)
	try:
		if ssl:
			url = 'https://' + url + '/'
		else:
			url = 'http://' + url + '/'
		driver.get(url)
		if driver.current_url != url:
			return False, driver.current_url
	except Exception as e:
		return False, 'error: ' + str(e)
	finally:
		driver.close()
>>>>>>> 20058ab4d24d2a1a1689c0dda3cbd299fc6cc018

def testSecurity(url):
	driver = webdriver.Chrome('chromedriver.exe')
	try:
		driver.get('https://xseo.in/viruscan')
		elem = driver.find_element_by_name("url")
		elem.send_keys(url)
		elem.send_keys(Keys.RETURN)
		elem = driver.find_elements_by_class_name("cls8")

		repa = elem[23].text.split()[2][1:-1]

		if elem[33].text == 'OK':
			YandexSerch = True
		else:
			YandexSerch = False

		return repa, YandexSerch
	except Exception as e:
		return False, 'error: ' + str(e)
	finally:
		driver.close()


def testBlackList(url):
	driver = webdriver.Chrome('chromedriver.exe')
	try:
		driver.get('https://sitecheck.sucuri.net/results/' + url)
		elem = driver.find_element_by_class_name('padding-left-35')
		res = elem.find_element_by_tag_name('h2')
		if res.text == 'Site is not Blacklisted':
			return True, res.text
		if res.text == 'Site is Blacklisted':
			return False, res.text
		return False, 'err: '+res.text
	except Exception as e:
		return False, 'error: ' + str(e)
	finally:
		driver.close()


def domen(url):
	if url.find('//') != -1:
		url = url[url.find('//')+2:]
	while url.rfind('/') != -1:
		url = url[:url.rfind('/')]
	c = url.count('.')+1
	if c > 2:
		return False, ??
	else:
		return True, c


def findDubl(url):
    driver = webdriver.Chrome('chromedriver.exe')
    try:
        driver.get('https://www.google.ru/search?q=' + url)
        elem = driver.find_elements_by_class_name('card-section')
        if len(elem) > 0:
            return False, elem[0].find_element_by_tag_name('a').text
        else:
            return True, 'OK'
    except Exception as e:
        return False, 'error: ' + str(e)
    finally:
        driver.close()


def cloneCheck(domain):
	try:	
		file = open('domains.txt', 'r')
		for line in file.readlines():
			unmatch = 0
			line = line[:-1]
			if line == domain:
				file.close()
				return True, 'OK'
			for index in range(min(len(domain), len(line))):
				if domain[index] != line[index]:
					unmatch += 1
			procent = unmatch / len(domain)
			if procent <= 0.25 / (1 + (len(domain) // 10)):
				file.close()
				return False, line
		return True, 'OK'
	except Exception as e:
		return False, 'err' + str(e)



if __name__ == '__main__':

<<<<<<< HEAD
    url = 'google.com'
    print(findDubl(url))
    print(checkSSL(url))
    print(testRedirection(url))
    print(checkValidDate(url, 14))
    print(testBlackList(url))
    print(testSecurity(url))
    print(scanDatabaseOpenphish(url))
    print(domen(url))
    print(findDubl(url))
=======
	url = 'google.com'	
	print(checkSSL(url))
	print(testRedirection(url))
	print(testBlackList(url))
	print(testSecurity(url))
	print(scanDatabaseOpenphish(url))
	print(domen(url))
	print(cloneCheck(url))
	print(findDubl(url))
	print(checkValidDate(url, 14))
>>>>>>> 20058ab4d24d2a1a1689c0dda3cbd299fc6cc018
