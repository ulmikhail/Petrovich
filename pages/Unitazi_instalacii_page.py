# from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base


class Unitazi_instalacii_page(Base):


        ### Lokators

    unitazi = '//*[@id="jsx-pet-app"]/div[1]/div[1]/div[1]/aside/nav/ul/li[2]/ul/li[1]/a/span/span[1]'
    unitazi_word = '//*[@id="jsx-pet-app"]/div[1]/header/div/h1'


        ### Getters

    def get_unitazi(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.unitazi)))

    def get_unitazi_word(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.unitazi_word)))


        ### Actions

    def click_unitazi(self):
        self.get_unitazi().click()
        print("Click unitazi")


        ## Methods
    def enter_unitazi(self):
        self.get_current_url()
        self.click_unitazi()
        self.assert_word(self.get_unitazi_word(), "Унитазы")


