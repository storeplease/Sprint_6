from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]/p'
    QUESTION_TO_SCROLL = By.XPATH, '//*[@id="accordion__heading-7"]' # only for scroll
    COOKIE_BUTTON = By.XPATH,'//*[@id="rcc-confirm-button"]'
