from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


def has_results(url):

    driver = webdriver.Chrome()
    driver.get(url)

    consent_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-button.fc-cta-consent.fc-primary-button")))
    consent_button.click()

    search_bar_img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "img-responsive")))
    search_bar_img.click()

    search_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "gsc-i-id1")))
    search_bar.send_keys("ocaml")
    search_bar.send_keys(Keys.ENTER)

    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No Results')]")))
        return False
    except:
        try:
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'verify')]")))
            sleep(60)
            driver.close()
            has_results(url)
        except:
            return True
