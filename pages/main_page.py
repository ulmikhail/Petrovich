
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base


class Main_page(Base):
    url = 'https://petrovich.ru/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ### Lokators

    catalog = '//*[@id="jsx-header"]/header/div[3]/div/div/aside/button'
    santehnika = 'body > div.pt-dropdown-popup___fyF3p.sections-menu-popup.pt-dropdown-popup-align-left___rJppR.pt-dropdown-popup-bottom___viyGt.pt-dropdown-popup-in-body___pVEKG > div > div.sections-menu-aside > div.sections-menu-top > ul:nth-child(1) > li:nth-child(6) > a'
    santehnika_word = '//*[@id="jsx-pet-app"]/div/h1'


        ### Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_santehnika(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.CSS_SELECTOR, self.santehnika)))

    def get_santehnika_word(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.santehnika_word)))


        ### Actions


    def click_catalog(self):
        self.get_catalog().click()
        print("Click Catalog")


    def click_santehnika(self):
        self.get_santehnika().click()
        print("Click Santehnika")


        ## Methods
    def enter_petrovich(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.click_catalog()
        self.click_santehnika()
        self.assert_word(self.get_santehnika_word(), "Сантехника")


