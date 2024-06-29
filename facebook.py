from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def tryClick(element, driver):
        try:
            actions = ActionChains(driver)
            clickable_el = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(element))
            actions.move_to_element(clickable_el).click().perform
            return True
        except WebDriverException:
            print("Element is not clickable")
            return False

if __name__ == "__main__":
    driver = webdriver.Edge()

    try:
        driver.get("https://www.facebook.com/")
        if driver.title == "Facebook – log in or sign up":
            print("waiting for facebook to login")
            try:
                cookie_dialogue = driver.find_element(By.XPATH, "//div[@data-testid='cookie-policy-manage-dialog']")
                WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((cookie_dialogue)))
                print('cookies closed')
                WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Friends']")))
                print('Logged in')
            except Exception as e:
                print(e)
                driver.quit()

            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Your profile']")))
                profile = driver.find_element(By.XPATH, "//a[@aria-label='Your profile']")
                profile.click()
                print('logging out')
            except Exception as e:
                print(e)

        time.sleep(100)
        driver.save_screenshot('screen.png')
    except Exception as e:
        print(e)

    driver.quit()