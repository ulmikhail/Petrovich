
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains


class Final_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ### Lokators

    cancel_order = '//*[@id="jsx-pet-app"]/div/div/div[2]/div[1]/div[1]/div/button[2]/span'
    final_price = '//*[@id="jsx-pet-app"]/div/div/div[2]/div[2]/div[1]/div[4]/ul/li/div[2]/div/div/div/p[2]'
    final_product = '//*[@id="jsx-pet-app"]/div/div/div[2]/div[2]/div[1]/div[4]/ul/li/div[2]/div/div/a/p'
    yes_cancel_order = '/html/body/div[6]/div/div/div/button[1]'


        ### Getters

    def get_cancel_order(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable((By.XPATH, self.cancel_order)))

    def get_final_price(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.final_price)))

    def get_final_product(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.final_product)))

    def get_yes_cancel_order(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable((By.XPATH, self.yes_cancel_order)))



        ### Actions


    def info_product_in_finish(self):
        print("Товар к оплате: " + self.get_final_product().text)

    def info_price_in_finish(self):
        print("Цена товара к оплате: " + self.get_final_price().text)

    def click_btn_cancel_order(self):
        self.get_cancel_order().click()
        print("Click btn 'Отмена заказа'")

    def click_btn_yes_cancel_order(self):
        self.get_yes_cancel_order().click()
        print("Click btn 'Да, отменить заказ'")


        ## Methods
    def cancel_orders(self):
        self.get_current_url()
        self.info_product_in_finish()
        self.info_price_in_finish()
        self.assert_product(self.get_final_product(), 'Унитаз-компакт GESSO Home de luxe W102 с косым выпуском c сиденьем пластик')
        self.assert_price(self.get_final_price(), '4 590 ₽')
        self.get_screenshot()
        time.sleep(5)
        self.click_btn_cancel_order()
        self.click_btn_yes_cancel_order()
        time.sleep(10)
        self.get_screenshot()







