from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
button = browser.find_element(By.ID, 'book')
button.click()

input_value = browser.find_element(By.ID, "input_value").text
y = calc(input_value)

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)

button2 = browser.find_element(By.ID, "solve")
button2.click()

time.sleep(10)
browser.quit()
