from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re

# Just don't bother with local weddriver rn, use `docker compose up -d`"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Remote(
	command_executor='http://localhost:4444/wd/hub',
	options=options
)

driver.get('https://www.civilservicejobs.service.gov.uk/csr/index.cgi')

try:
	# get total jobs by location
	location = "Bristol"
	where = driver.find_element(By.ID, "whereselector")
	where.send_keys(location)
	driver.find_element(By.ID, "submitSearch").click()
	searchResults = driver.find_element(By.ID, "id_common_page_title_h1").get_attribute("innerText")
	cleaned_text = re.sub(r'[^0-9]', '', searchResults)
	try:
		number = int(cleaned_text)
		print(f"Total Jobs reported found: {number}")
	except ValueError:
		print("Unable to extract a valid number.")

	# extract pages (don't include the "next page" link)
	pages = {}
	for a in driver.find_element(By.CSS_SELECTOR, ".search-results-paging-menu").find_elements(By.TAG_NAME, "a"):
		page = a.get_attribute("innerText")
		link = a.get_attribute("href")
		match = re.search(r"\d+", page)
		if match:
			number = int(match.group())
			if page not in pages:
				pages[page] = {"page": number, "link": link}

	# extract job listings
	for job in driver.find_elements(By.CSS_SELECTOR, ".search-results-job-box"):
		title = job.find_element(By.CSS_SELECTOR, ".search-results-job-box-title")
		salary = job.find_element(By.CSS_SELECTOR, ".search-results-job-box-salary")
		print(f"title: {title.get_attribute('innerText')}")
		print(f"salary range: {salary.get_attribute('innerText')}")

except Exception as e:
	print(e)

time.sleep(10)
driver.quit()