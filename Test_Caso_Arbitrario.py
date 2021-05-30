import sys
import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestRetoFinalCaso(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_reto_final_caso_arbitrario1(self):

        driver = self.driver
        driver.get("https://demoqa.com/radio-button")
        time.sleep(2)
        radio_button = driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]")
        radio_button.click()
        time.sleep(2)
        texto_encontrado = driver.find_element_by_xpath("//span[contains(text(),'Impressive')]")
        self.assertEqual(texto_encontrado.text,"Impressive")
        time.sleep(1)

        # codigo here!

    def test_reto_final_caso_arbitrario2(self):
        driver = self.driver
        driver.get("https://demoqa.com/buttons")
        time.sleep(2)
        boton_doble_click = driver.find_element_by_xpath("//button[@id='doubleClickBtn']")
        boton_click_derecho = driver.find_element_by_xpath("//button[@id='rightClickBtn']")
        boton_solo_click = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div[3]/button")

        time.sleep(1)
        action = ActionChains(driver)
        action.double_click(boton_doble_click).perform()

        time.sleep(1)
        action = ActionChains(driver)
        action.context_click(boton_click_derecho).perform()

        time.sleep(1)
        boton_solo_click.click()
        time.sleep(1)

        texto_doble_click = driver.find_element_by_xpath("//p[@id='doubleClickMessage']")
        texto_click_derecho = driver.find_element_by_xpath("//p[@id='rightClickMessage']")
        texto_click = driver.find_element_by_xpath("//p[@id='dynamicClickMessage']")

        self.assertEqual(texto_click.text,"You have done a dynamic click")
        self.assertEqual(texto_click_derecho.text,"You have done a right click")
        self.assertEqual(texto_doble_click.text,"You have done a double click")
        time.sleep(1)

        # codigo here!
    def test_reto_final_caso_arbitrario3(self):
        driver = self.driver
        driver.get("https://demoqa.com/links")

        time.sleep(1)
        nueva_ventana = driver.find_element_by_xpath("//a[@id='simpleLink']")
        nueva_ventana.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        link_created = driver.find_element_by_xpath("//a[@id='created']")
        link_created.click()
        driver.execute_script("window.scrollTo(0, 130)")
        time.sleep(2)
        mensaje_created = driver.find_element_by_xpath("//p[@id='linkResponse']")
        time.sleep(2)
        self.assertRegex(mensaje_created.text,"201")

        # codigo here!
    def test_reto_final_caso_arbitrario4(self):
        driver = self.driver
        driver.get("https://demoqa.com/broken")

        time.sleep(2)
        nueva_ventana = driver.find_element_by_xpath("//a[contains(text(),'Click Here for Valid Link')]")
        nueva_ventana.click()
        time.sleep(2)
        driver.back()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 90)")
        time.sleep(1)
        link_broken = driver.find_element_by_xpath("//a[contains(text(),'Click Here for Broken Link')]")
        link_broken.click()
        time.sleep(2)
        driver.back()
        time.sleep(1)

        # codigo here!
    def test_reto_final_caso_arbitrario5(self):
        driver = self.driver
        driver.get("https://demoqa.com/upload-download")
        time.sleep(2)
        descargar = driver.find_element_by_xpath("//a[@id='downloadButton']")
        descargar.click()
        time.sleep(3)
        full_path = os.path.realpath(__file__)
        driver.find_element_by_id("uploadFile").send_keys(os.path.dirname(full_path) + "\sampleFile.jpeg")
        time.sleep(1)
        archivo_subido = driver.find_element_by_xpath("//p[@id='uploadedFilePath']")
        time.sleep(1)
        self.assertRegex(archivo_subido.text, "sampleFile.jpeg")

        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
