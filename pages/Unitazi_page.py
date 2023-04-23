
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base


class Unitazi_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ### Lokators

    price_do = '//*[@id="pt-input-id-2"]'
    brend_gesso = "//label[@for='gesso']"
    product = '//*[@id="product-list-content"]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div[1]/a/span'
    price = '//*[@id="product-list-content"]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/div/p'
    btn_v_korzinu = '//*[@id="product-list-content"]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/a/span'
    go_to_kart = "//a[@class='header-cart qty']"
    kart_word = '//*[@id="jsx-pet-app"]/div/div/h1'


        ### Getters

    def get_price_do(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable((By.XPATH, self.price_do)))

    def get_brend_gesso(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable((By.XPATH, self.brend_gesso)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable((By.XPATH, self.product)))

    def get_price(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.price)))

    def get_btn_v_korzinu(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.btn_v_korzinu)))

    def get_go_to_kart(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.go_to_kart)))

    def get_kart_word(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.kart_word)))


        ### Actions


    def input_prise_do(self, price_do):
        self.get_price_do().send_keys(price_do)
        print("Input price do 5000")
        time.sleep(3)

    def click_brend_gesso(self):
        self.get_brend_gesso().click()
        time.sleep(3)
        print("brend Gesso")

    def info_product(self):
        print("Товар: " + self.get_product().text)

    def info_price(self):
        print("Цена: " + self.get_price().text)

    def click_btn_v_korzinu(self):
        self.get_btn_v_korzinu().click()
        print("Click btn 'В корзину'")
        time.sleep(3)

    def click_go_to_kart(self):
        self.get_go_to_kart().click()
        print("Go to kart")
        time.sleep(3)


        ## Methods
    def vybor_tovara (self):
        self.get_current_url()
        self.input_prise_do(5000)
        self.scroll_down()
        self.click_brend_gesso()
        self.scroll_up()
        self.info_product()
        self.info_price()
        self.click_btn_v_korzinu()
        self.click_go_to_kart()
        self.assert_word(self.get_kart_word(), "Корзина")


