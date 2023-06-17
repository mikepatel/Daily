"""
"""
################################################################################
# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from time import sleep

import config


################################################################################
# click on button
def click_button(driver, xpath):
    sleep(5)
    button = driver.find_element_by_xpath(xpath)
    button.click()


################################################################################
# Main
if __name__ == "__main__":
    # open driver
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path=config.chromedriver_path,
        options=chrome_options
    )
    driver.get(config.url)

    # username
    username = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "login_field"))
    )
    username.send_keys(config.username)

    # password
    pw = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "password"))
    )
    pw.send_keys(config.password)

    # sign in button
    signin = driver.find_element_by_name("commit")
    signin.send_keys(Keys.ENTER)

    # edit README
    xpath = '/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[2]/div[1]/div/div/main/div[2]/div/div[3]/div[2]/div/div[2]/file-attachment/div/div/div[2]/div[2]/div[2]/br'

    text = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, xpath))
    )
    text.send_keys(Keys.DELETE)

    # scroll down page
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # commit button
    button_xpath = '/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[2]/div[1]/div/div/main/div[2]/div/div[3]/div[1]/div[2]/button/span/span'
    click_button(driver, button_xpath)

    # confirmation button
    button_xpath = '/html/body/div[1]/div[6]/div/main/turbo-frame/div/react-app/div/div/div[1]/div/div/div/div[3]/button[2]'
    click_button(driver, button_xpath)

    # close driver
    driver.close()
    driver.quit()