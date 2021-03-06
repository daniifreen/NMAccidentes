import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time

#### pruebas de ingresar 
class usando_unitest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\DriveSele\chromedriver.exe")
# Inicio de crear Cliente
    def test_Crear_Cliente(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        self.assertIn("Login", driver.title)
        usuario = driver.find_element_by_id("id_username")
        usuario.send_keys("Benja")
        clave = driver.find_element_by_id("id_password")
        clave.send_keys("duoc123456")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.get("http://127.0.0.1:8000/servicios.html")
        time.sleep(2)
        time.sleep(2)
        driver.get("http://127.0.0.1:8000/crearCliente.html")
        time.sleep(2)
        self.assertIn("Ingresar Cliente", driver.title)
        rut = driver.find_element_by_id("txtRut")
        rut.send_keys("197927039")
        nombre = driver.find_element_by_name("nombre")
        nombre.send_keys("Cliente")
 # seleccionar en un select
        Seleccionar = Select(driver.find_element_by_name("rubro"))
        Seleccionar.select_by_value("4")
        direccion = driver.find_element_by_name("direccion")
        direccion.send_keys("Callefalsa123")
        time.sleep(2)
        direccion.send_keys(Keys.ENTER)
        time.sleep(2)
        username = driver.find_element_by_id("id_username")
        username.send_keys("Cliente")
        contraa = driver.find_element_by_id("id_password1")
        contraa.send_keys("duoc123456")
        contras = driver.find_element_by_id("id_password2")
        contras.send_keys("duoc123456")
        email = driver.find_element_by_id("id_email")
        email.send_keys("pruebaClie@gmail.com")
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        if driver.current_url=='http://127.0.0.1:8000/register_Cliente.html':
            print("Se ha creado el Cliente con exito en el sistema ")
        else:
            print("no se pudo ingresar el Cliente")

    def cerrar3(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()