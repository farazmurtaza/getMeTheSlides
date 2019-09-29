
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import config


class GoogleSlidesBot():
    def __init__(self, email, password):
        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        self.browser = webdriver.Chrome(chrome_options=options)
        #actions = ActionChains(self.driver)
        # self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        actions = ActionChains(self.browser)
        self.browser.get(
            'https://docs.google.com/presentation/d/1rG3IFitUfjJhc9p3-XOWHBK9L6ayTWpObZrDDX2jAXA/edit?ts=5d8f1ab7#slide=id.p')

        emailInput = self.browser.find_elements_by_css_selector('form input')[
            0]
        # passwordInput = self.browser.find_elements_by_css_selector('form input')[
        #     1]

        emailInput.send_keys(self.email)
        # passwordInput.send_keys(self.password)
        emailInput.send_keys(Keys.ENTER)
        time.sleep(2)

        passwordInput = self.browser.find_elements_by_css_selector('form input')[
            2]
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        time.sleep(2)

        slideShowButton = self.browser.find_element_by_id(
            'punch-start-presentation-left')
        time.sleep(5)

        slideShowButton.click()

        time.sleep(2)

        # rightArrowKey = self.browser.find_element_by_css_selector(
        #     'punch-viewer-icon punch-viewer-right goog-inline-block')
        # time.sleep(5)
        # rightArrowKey.click()
        actions.send_keys(Keys.ARROW_RIGHT)
        for i in range(200):
            time.sleep(0.5)
            actions.perform()


bot = GoogleSlidesBot(config.username, config.password)
bot.signIn()
