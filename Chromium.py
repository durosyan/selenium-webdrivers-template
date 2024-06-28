import time
from selenium import webdriver
from pathlib import Path

# chromium portal only opens "data;"
# https://github.com/SeleniumHQ/selenium/issues/8061

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
