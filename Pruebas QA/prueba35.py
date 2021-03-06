import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
#rver_listado_solicitudes_cliente
    def test_ver_listado_solicitudes_cliente(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Cliente")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        # ir a servicios
        driver.find_element_by_xpath("/html/body/header/div/nav/ul/li[4]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/main/section/div/section[1]/div/div/div[1]/div/div[3]/input").click()
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/listadosolcliente.html/3':
            print("Se mostro todas las solicitudes que realizo el cliente ")
        else:
            print("No Se mostro las solicitudes  ")

    def cerrar7(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()