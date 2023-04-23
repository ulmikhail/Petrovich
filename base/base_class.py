
import datetime
import time

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        vallue_word = word.text
        assert vallue_word == result
        print("Good value word")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method assert product"""

    def assert_product(self, word, result):
        vallue_word = word.text
        assert vallue_word == result
        print("Good value product")

    """Method assert price"""

    def assert_price(self, word, result):
        vallue_word = word.text
        assert vallue_word == result
        print("Good value price")


    """Method scroll down"""

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 1700)")
        time.sleep(3)
        print("Scroll down")

    """Method scroll down 2"""

    def scroll_down_2(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        print("Scroll down 2")

    """Method scroll up"""

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(3)
        print("Scroll up")

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y. %H.%M.%S")
        name_skrin = 'skrinshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\Petrovich\\screens\\' + name_skrin)

