import re
import sys
import unittest
import time
from selenium import webdriver


class TestRetoFinalCaso(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.close()

    def test_reto_final_caso_arbitrario1(self):
        driver = self.driver
        driver.get("http://www.rpachallenge.com/")
        boton_start = driver.find_element_by_xpath("//button[contains(text(),'Start')]")
        boton_start.click()
        time.sleep(2)

        nombre_lista = ["John", "Jane", "Albert", "Michael", "Doug", "Jessie", "Stan", "Michelle", "Stacy", "Lara"]
        apellido_lista = ["Smith", "Dorsey", "Kipling", "Robertson", "Derrick", "Marlowe", "Hamm", "Norton", "Shelby","Palmer"]
        company_lista = ["IT Solutions", "MediCare", "Waterfront", "MediCare", "Timepath Inc.", "Aperture Inc.","Sugarwell", "Aperture Inc.", "TechDev", "Timepath Inc."]
        role_lista = ["Analyst", "Medical Engineer", "Accountant", "IT Specialist", "Analyst", "Scientist", "Advisor","Scientist", "HR Manage", "Programmer"]
        direccion_lista = ["98 North Road", "11 Crown Street", "22 Guild Street", "17 Farburn Terrace","99 Shire Oak Road", "27 Cheshire Street", "10 Dam Road", "13 White Rabbit Street","19 Pineapple Boulevard", "87 Orange Street"]
        email_lista = ["jsmith@itsolutions.co.uk", "jdorsey@mc.com", "kipling@waterfront.com", "mrobertson@mc.com", "dderrick@timepath.co.uk", "jmarlowe@aperture.us", "shamm@sugarwell.org", "mnorton@aperture.us","sshelby@techdev.com", "lpalmer@timepath.co.uk"]
        telefono_lista = ["40716543298", "40791345621", "40735416854", "40733652145", "40799885412", "40733154268","40712462257", "40731254562", "40741785214", "40731653845"]


        for nombre, apellido, compania, role, direccion, email, telefono in zip(nombre_lista,apellido_lista,company_lista,role_lista,direccion_lista,email_lista,telefono_lista):
            input_nombre = driver.find_element_by_css_selector("[ng-reflect-name=labelFirstName]")
            input_apellido = driver.find_element_by_css_selector("[ng-reflect-name=labelLastName]")
            input_compania = driver.find_element_by_css_selector("[ng-reflect-name=labelCompanyName]")
            input_role = driver.find_element_by_css_selector("[ng-reflect-name=labelRole]")
            input_direccion = driver.find_element_by_css_selector("[ng-reflect-name=labelAddress]")
            input_email = driver.find_element_by_css_selector("[ng-reflect-name=labelEmail]")
            input_telefono = driver.find_element_by_css_selector("[ng-reflect-name=labelPhone]")

            boton_submit = driver.find_element_by_xpath("//body/app-root[1]/div[2]/app-rpa1[1]/div[1]/div[2]/form[1]/input[1]")

            input_nombre.send_keys(nombre)
            input_apellido.send_keys(apellido)
            input_compania.send_keys(compania)
            input_role.send_keys(role)
            input_direccion.send_keys(direccion)
            input_email.send_keys(email)
            input_telefono.send_keys(telefono)
            boton_submit.click()

        time.sleep(5)
        porcentaje = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]")
        pattern = '\d+'
        result = re.findall(pattern, porcentaje.text)
        self.assertGreater(int(result.__getitem__(0)),90)


if __name__ == '__main__':
    unittest.main()