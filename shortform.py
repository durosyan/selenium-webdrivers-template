from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
import time


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    # Set the remote webdriver URL
    webdriver_url = "http://localhost:4444/wd/hub"

    try:
        # Navigate to the Shortform website
        print("Navigating to Shortform website")
        driver.get("https://www.shortform.com/app/login")

        print("Checking the title of the page")
        print(driver.title == "Shortform | Login")

        print("Checking the color of the login button")
        login_email_button = driver.find_element(By.ID,'login_email')
        login_password_button = driver.find_element(By.ID,'login_password')
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log In')]")
        print(Color.from_string('rgba(255, 201, 6, 1)') == Color.from_string(login_button.value_of_css_property('background-color')))

        print("Entering the email and password")
        login_email_button.send_keys("...")
        login_password_button.send_keys("...")

        print("Clicking the login button")
        login_button.click()

        print("Checking the title of the page")
        print(driver.title == "Shortform | Login")

        # Wait for 30 minutes
        time.sleep(1800)
    except Exception as e:
        print(e)

    driver.quit()