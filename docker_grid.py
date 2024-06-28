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
            color = Color.from_string(element.value_of_css_property('background-color'))
            print(color)
            return True
        except WebDriverException:
            print("Element is not clickable")
            return False

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
        command_executor='http://localhost:9515/wd/hub',
        options=options
    )

    try:
        # Navigate to the Shortform website
        print("Navigating")
        driver.get("https://www.facebook.com/")

        print("Checking the title of the page: ", driver.title == "Facebook – log in or sign up")

        print("Clicking accept cookies")
        cookie_accept_label = driver.find_element(By.XPATH, "//div[@role='button'][@aria-label='Allow all cookies']")
        cookie_accept_children = cookie_accept_label.find_elements(By.XPATH, './/*');
        cookie_accept = cookie_accept_children[1]
        tryClick(cookie_accept_label, driver)
        

        time.sleep(2)

        print("Saving screenshot")
        driver.save_screenshot('screen.png')

        print("Checking the color of the login button")
        login_email_button = driver.find_element(By.ID,'email')
        login_password_button = driver.find_element(By.ID,'pass')

        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")

        # print(Color.from_string('rgb(8, 102, 255)') == Color.from_string(login_button.value_of_css_property('background-color')))

        print("Entering the email and password")
        # login_email_button.send_keys("+447432561513")
        # login_password_button.send_keys("z^y5(6gs$h0.SfaK#V0,")

        print("Clicking the login button")
        # login_button.click()

        # Wait for 30 minutes
        # time.sleep(1800)
    except Exception as e:
        print(e)

    driver.quit()