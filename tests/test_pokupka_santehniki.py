
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.Unitazi_instalacii_page import Unitazi_instalacii_page
from pages.Unitazi_page import Unitazi_page
from pages.cart_page import Cart_page
from pages.delivery_page import Delivery_page
from pages.final_page import Final_page
from pages.main_page import Main_page
from pages.santehnika_page import Santehnika_page
from pages.self_page import Self_page


def test_buy_product(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\resource\\chromedriver.exe', chrome_options=options)
    driver.set_window_size(1400, 1300)
    print('Start test')

    mp = Main_page(driver)
    mp.enter_petrovich()

    sp = Santehnika_page(driver)
    sp.enter_unitazi_installacii()

    uip = Unitazi_instalacii_page(driver)
    uip.enter_unitazi()

    unitazi = Unitazi_page(driver)
    unitazi.vybor_tovara()

    cp = Cart_page(driver)
    cp.order_product()

    dp = Delivery_page(driver)
    dp.enter_to_samovivoz()

    self_p = Self_page(driver)
    self_p.checkout()

    fp = Final_page(driver)
    fp.cancel_orders()

    print('Finish test')
    time.sleep(5)