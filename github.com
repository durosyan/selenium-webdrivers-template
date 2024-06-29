from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if (__name__ == "__main__"):
	driver = webdriver.Edge()
	driver.get('https://github.com/durosyan?tab=repositories')

	# Gather data
	data = {
	    # 'profile_name': driver.find_element(By.CLASS_NAME, 'vcard-fullname'),
	    'repositories': driver.find_element(By.ID, "user-repositories-list")
	    # 'projects': driver.find_elements(By.XPATH, '//div[contains(@class, "projects")]'),
	    # 'packages': driver.find_elements(By.XPATH, '//div[contains(@class, "packages")]'),
	    # 'stars': driver.find_elements(By.XPATH, '//div[contains(@class, "stars")]')
	}

	# Process and print the data
	for key, elements in data.items():
	    print(f"{key}:")
	    for element in elements:
	        print(f" - {element.text}")

	time.sleep(2)
	driver.quit()

