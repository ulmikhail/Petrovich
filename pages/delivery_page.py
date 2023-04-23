# from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base



class Delivery_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


        ### Lokators

    go_somovyvoz = '//*[@id="jsx-cart"]/div/div[1]/div/ul/li[2]/a'
    confirm_btn = '//*[@id="delivery_final_scrolled"]/div/div/input'


        ### Getters

    def get_go_somovyvoz(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.go_somovyvoz)))

    def get_confirm_btn(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.confirm_btn)))


        ### Actions


    def click_samovivoz(self):
        self.get_go_somovyvoz().click()
        print("Click Самовывоз")


        ## Methods

    def enter_to_samovivoz(self):
        self.get_current_url()
        self.assert_url("https://petrovich.ru/cart/order/fiz/delivery/")
        self.click_samovivoz()
        self.get_current_url()
        self.assert_url("https://petrovich.ru/cart/order/fiz/self/")




