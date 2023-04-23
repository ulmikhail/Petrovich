
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base



class Santehnika_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ### Lokators

    unitazi_installacii = '//*[@id="jsx-pet-app"]/div/div[1]/div[1]/aside/nav/ul/li[6]/a/span'
    unitazi_installacii_word = '//*[@id="jsx-pet-app"]/div[1]/header/div/h1'


        ### Getters

    def get_unitazi_installacii(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.unitazi_installacii)))

    def get_unitazi_installacii_word(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.unitazi_installacii_word)))


        ### Actions


    def click_unitazi_installacii(self):
        self.get_unitazi_installacii().click()
        print("Click unitazi i installacii")


        ## Methods
    def enter_unitazi_installacii(self):
        self.get_current_url()
        self.click_unitazi_installacii()
        self.assert_word(self.get_unitazi_installacii_word(), "Унитазы, инсталляции и писсуары")


