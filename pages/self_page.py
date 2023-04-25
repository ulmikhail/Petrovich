import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from base.base_class import Base


class Self_page(Base):

        ### Lokators

    radio_btn_place = '//*[@id="tab_delivery"]/ol/li[1]/div/div/ul/li[1]/label/div'
    payment_btn = '//*[@id="tab_delivery"]/ol/li[3]/div/div/div[1]/div/label/span[2]'
    way_to_get = '//*[@id="tab_delivery"]/ol/li[4]/div/div[2]/div/label'
    email = '//*[@id="tab_delivery"]/ol/li[5]/div/div/input'
    phone = "//input[@name='contactsPhone']"
    name = "//input[@name='contactsName']"
    finish_price = '//*[@id="delivery_final_scrolled"]/div/div/p[2]/p'
    confirm_btn = '//*[@id="delivery_final_scrolled"]/div/div/input'


        ### Getters

    def get_radio_btn_place(self):
        return WebDriverWait(self.driver, 20).until(ES.element_to_be_clickable((By.XPATH, self.radio_btn_place)))

    def get_payment_btn(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.payment_btn)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.email)))

    def get_way_to_get(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.way_to_get)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.phone)))

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.name)))

    def get_confirm_btn(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.confirm_btn)))

    def get_finish_price(self):
        return WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable((By.XPATH, self.finish_price)))


       ### Actions


    def click_radio_btn_place(self):
        self.get_radio_btn_place().click()
        print("Выбор места самовывоза")

    def click_payment_btn(self):
        self.get_payment_btn().click()
        print("Выбор оплаты")

    def click_way_to_get(self):
        self.get_way_to_get().click()
        print("Способ получения")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input mail")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone")
    def input_name(self, name):
        self.get_name().send_keys(name)
        print("Input name")

    def click_confirm_btn(self):
        self.get_confirm_btn().click()
        print("Click confirm btn")

    def info_finish_price(self):
        print("Цена на финише: " + self.get_finish_price().text)


        ## Methods

    def checkout(self):
        self.click_radio_btn_place()
        self.scroll_down_2()
        self.click_payment_btn()
        self.click_way_to_get()
        self.input_email('qwer1@mail.ru')
        self.input_name('Mike')
        self.input_phone("89031771234")
        self.info_finish_price()
        self.assert_price(self.get_finish_price(), '4 590 ₽')
        self.click_confirm_btn()







