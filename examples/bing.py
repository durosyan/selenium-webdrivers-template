from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import re

driver = webdriver.Edge()

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

def extract_number_from_text(text):
    # Remove any non-digit characters (including commas)
    cleaned_text = re.sub(r'[^0-9]', '', text)
    # Convert the cleaned text to an integer
    try:
        number = int(cleaned_text)
        return number
    except ValueError:
        return None  # Unable to extract a valid number

try:
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "b_results")))
	element = driver.find_element(By.ID, "b_tween_searchResults")
	searchResults = element.get_attribute("innerText")
	extracted_number = extract_number_from_text(searchResults)
	if extracted_number is not None:
	    print(f"Extracted number: {extracted_number}")
	else:
	    print("Unable to extract a valid number.")
except Exception as e:
	print(e)

driver.quit()