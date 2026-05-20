from selenium.webdriver.common.by import By

class ExternalNavigationLocators:
    SCOOTER_LOGO = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]'
    YANDEX_LOGO = By.XPATH, '//a[contains(@class, "Header_LogoYandex")]'
    YA_ELEMENT = By.XPATH, '//div[contains(@class, "search3__logo-inner")]'
    SCOOTER_ELEMENT = By.XPATH, '//div[contains(@class, "Home_Header")]'