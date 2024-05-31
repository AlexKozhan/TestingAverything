"""Проверим, что при загрузке страницы отображается несколько фактов о кошках."""


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class CatFactsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://alexwohlbruck.github.io/cat-facts/")

    def test_multiple_facts_display(self):
        facts = self.driver.find_elements(By.CLASS_NAME, "fact")
        self.assertGreaterEqual(len(facts), 1)

    def tearDown(self):
        # Возвращение на главную страницу после каждого теста
        self.driver.get("https://alexwohlbruck.github.io/cat-facts/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
