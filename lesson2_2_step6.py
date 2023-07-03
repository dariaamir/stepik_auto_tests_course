from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radio_button = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
radio_button.click()

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)
browser.quit()