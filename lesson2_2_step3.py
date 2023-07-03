from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum1 = str(num1 + num2)

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(sum1)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

