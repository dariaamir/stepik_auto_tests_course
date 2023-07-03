import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)
browser.quit()
