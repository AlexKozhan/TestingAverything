"""Проверим, что ссылка на страницу с информацией о
разработчике корректно работает и ведет на правильную страницу."""


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

    def test_developer_info_link(self):
        developer_link = self.driver.find_element(By.LINK_TEXT, "Developed by Alex Wohlbruck")
        developer_link.click()
        time.sleep(2)  # Ожидание перехода на страницу
        self.assertIn("https://github.com/alexwohlbruck/cat-facts", self.driver.current_url)

    def tearDown(self):
        # Возвращение на главную страницу после каждого теста
        self.driver.get("https://alexwohlbruck.github.io/cat-facts/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
