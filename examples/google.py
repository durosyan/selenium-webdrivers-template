import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    driver.get('https://www.google.com/');
    time.sleep(5) # Let the user actually see something!

    try:
        # element not interactable...
        search_box = driver.find_element(By.XPATH, "//textarea[@name='q']")
        search_box.send_keys('ChromeDriver')
        search_box.submit()
    except Exception as e:
        print(e)

    time.sleep(5) # Let the user actually see something!
    driver.quit()
