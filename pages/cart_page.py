
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains


class Cart_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ### Lokators

    product_in_cart = '//*[@id="jsx-pet-app"]/div/div/div[3]/div/div[2]/div[4]/p'
    price_in_cart = '//*[@id="jsx-pet-app"]/div/div/div[3]/div/div[2]/div[6]/div[1]/span/p'
    total_price = '//*[@id="cart-aside"]/div/div[2]/div[3]/div[2]/div[1]/div/p[2]'
    btn_order = '//*[@id="cart-aside"]/div/div[2]/div[3]/div[3]/div/button/span'


        ### Getters

    def get_product_in_cart(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.product_in_cart)))

    def get_price_in_cart(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.price_in_cart)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_btn_order(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.btn_order)))


        ### Actions


    def info_product_in_cart(self):
        print("Товар в корзине: " + self.get_product_in_cart().text)

    def info_price_in_cart(self):
        print("Цена товара в корзине: " + self.get_price_in_cart().text)

    def info_total_price(self):
        print("Итоговая цена: " + self.get_total_price().text)

    def click_btn_order(self):
        self.get_btn_order().click()
        print("Click btn 'Оформитиь'")
        time.sleep(3)


        ## Methods

    def order_product (self):
        self.get_current_url()
        self.info_product_in_cart()
        self.info_price_in_cart()
        self.info_total_price()
        self.assert_product(self.get_product_in_cart(), 'Унитаз-компакт GESSO Home de luxe W102 с косым выпуском c сиденьем пластик')
        self.assert_price(self.get_price_in_cart(), '4 590 ₽')
        assert self.get_price_in_cart().text == self.get_total_price().text
        print('total price - good!')
        self.click_btn_order()



