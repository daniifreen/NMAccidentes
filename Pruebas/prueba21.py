import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.chrome.options import Options
class usando_unitest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
#ver Accidentibilidad
    def test_ver_Accidentibilidad(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("admin")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("admin")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        #ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        #ir a ver Accidentibilidad
        driver.find_element_by_xpath("/html/body/main/section/div/div/div[5]/div/div[2]/input").click()
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/listadoAccidentibilidad.html':
            print("Se muestra el porcentaje de Accidentibilidad ")
        else:
            print("no muestra  Accidentibilidad")

    def cerrar9(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()