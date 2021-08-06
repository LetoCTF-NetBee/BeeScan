from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def testRedirection(url):
	driver = webdriver.Chrome('C:/Users/Larri/projects/CTF/selenium_test/chromedriver.exe')
	try:
		driver.get(url)
		if driver.current_url != url:
			return False, driver.current_url

	except Exception as e:
		return False, 'error: ' + str(e)
	finally:
		driver.close()
if __name__ == '__main__':
	print(testRedirection('http://larri.ru'))