from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    time.sleep(1)
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    radio_button.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

