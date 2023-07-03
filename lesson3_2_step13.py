import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):

    browser = webdriver.Chrome()
    url1 = 'http://suninjuly.github.io/registration1.html'
    url2 = 'http://suninjuly.github.io/registration2.html'

    welcome_text = "Congratulations! You have successfully registered!"

    def test_registration_1_happy_path(self):
        self.browser.get(url=self.url1)

        input_first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
        input_last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
        input_email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")


        input_first_name.send_keys("Ivan")
        input_last_name.send_keys("Petrov")
        input_email.send_keys("ivan_petrov@mail.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")

        self.assertEqual(welcome_text_elt.text, self.welcome_text), \
        f"Error: registration text is not correct. " \
        f"Actual: {welcome_text_elt.text}, expected: {self.welcome_text}"

    def test_registration_2_negative_flow(self):
        self.browser.get(url=self.url2)
        input_first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input")
        input_last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input")
        input_email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input")

        input_first_name.send_keys("Ivan")
        input_last_name.send_keys("Petrov")
        input_email.send_keys("ivan_petrov@mail.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")

        self.assertEqual(welcome_text_elt.text, self.welcome_text), \
        f"Error: registration text is not correct. " \
        f"Actual: {welcome_text_elt.text}, expected: {self.welcome_text}"


if __name__ == "__main__":
    unittest.main()