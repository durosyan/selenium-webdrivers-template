from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re

driver = webdriver.Edge()
driver.get('https://www.civilservicejobs.service.gov.uk/csr/index.cgi')

def extract_number_from_text(text):
    cleaned_text = re.sub(r'[^0-9]', '', text)
    try:
        number = int(cleaned_text)
        return number
    except ValueError:
        return None

def extract_pages(pages, paging_element):
	'''
	extract pages (pagination is truncated)
	'''


name = input("Enter your job search location: ")

try:
	where = driver.find_element(By.ID, "whereselector")
	where.send_keys(name)
	driver.find_element(By.ID, "submitSearch").click()
	searchResults = driver.find_element(By.ID, "id_common_page_title_h1").get_attribute("innerText")
	extracted_number = extract_number_from_text(searchResults)

	if extracted_number is not None:
	    print(f"Total Jobs reported found: {extracted_number}")
	else:
	    print("Unable to extract a valid number.")

	pages = {}

	for a in driver.find_element(By.CSS_SELECTOR, ".search-results-paging-menu").find_elements(By.TAG_NAME, "a"):
		page = a.get_attribute("innerText")
		link = a.get_attribute("href")
		match = re.search(r"\d+", page)
		if match:
			number = int(match.group())
			if page not in pages:
				pages[page] = {"page": number, "link": link}

	job_list = driver.find_elements(By.XPATH, "//ul[@title='Job list']")


except Exception as e:
	print(e)



time.sleep(10)

driver.quit()