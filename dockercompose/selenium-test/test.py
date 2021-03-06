# python test.py
# pip install selenium
#               requirements.txt


# 1 Arrancar el grid
# 2 Crear una imagen de conteendor con python3
#       Que tenga dentro mi programa 
#       y las librerias que hacen falta
#       Que ejecute mi programa
# 3 Crear un conteendor (docker-compose)
#   que ejecute el programa
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Tester(unittest.TestCase):
    def setUp(self):

        self.driver=webdriver.Remote(
            command_executor="http://172.31.14.171:4444",
            desired_capabilities={
                "browserName": "chrome"
            }
        )
        self.base_url = "http://172.31.14.171:8082/webapp/"
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test1(self):
        driver = self.driver
        driver.get("http://172.31.14.171:8082/webapp/")
        time.sleep(3)
        #---
        texto=driver.find_element(By.XPATH,"//h2").text
        #---
        self.assertEquals("Hola Jenkins!",texto)
        
        driver.get("https://phoenixnap.com/kb/install-docker-compose-ubuntu")
        driver.save_screenshot("/instantaneas/screenshot.png")

    def tearDown(self):
        self.driver.quit()

unittest.main()