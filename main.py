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

    # edit readme
    sleep(5)
    # xpath = '/html/body/div[5]/div/main/div[2]/div/div/form[2]/div/file-attachment/secret-scanning-blob/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[5]/div[2]/pre/span/span'
    # xpath = '/html/body/div[5]/div/main/div[2]/div/div[2]/form[2]/div/file-attachment/blob-editor/div[2]/div/div/div[5]/div[1]/div/div/div/div[5]/div[2]/pre/span'
    xpath = '/html/body/div[5]/div/main/turbo-frame/div/div/div[2]/form[2]/div/file-attachment/blob-editor/div[2]/div/div/div[5]/div[1]/div/div/div/div[5]/div[2]/pre/span/span'
    xpath = '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div[2]/form[2]/div/file-attachment/blob-editor/div[2]/div/div/div[5]/div[1]/div/div/div/div[5]/div[2]/pre/span/span'
    text = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.XPATH, xpath))
    )
    
    text.send_keys(Keys.BACK_SPACE)

    # scroll down page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # commit button
    button = driver.find_element_by_id("submit-file")
    button.send_keys(Keys.ENTER)

    # close driver
    driver.close()
    driver.quit()
