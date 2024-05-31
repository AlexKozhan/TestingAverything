"""Проверим, что кнопка для обновления факта о кошках работает корректно."""


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CatFactsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://alexwohlbruck.github.io/cat-facts/")

    def test_refresh_fact(self):
        initial_fact = self.driver.find_element(By.CLASS_NAME, "cat-fact").text
        refresh_button = self.driver.find_element(By.CLASS_NAME, "refresh-button")
        refresh_button.click()
        time.sleep(2)  # Ожидание обновления факта
        new_fact = self.driver.find_element(By.CLASS_NAME, "cat-fact").text
        self.assertNotEqual(initial_fact, new_fact)

    def tearDown(self):
        # Возвращение на главную страницу после каждого теста
        self.driver.get("https://alexwohlbruck.github.io/cat-facts/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
