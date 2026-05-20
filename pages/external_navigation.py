import allure
from locators.external_navigation_locators import ExternalNavigationLocators
from pages.base_page import BasePage

class ExternalNavigation(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ExternalNavigationLocators
    
    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_to_element(self.locators.SCOOTER_LOGO)
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_to_element(self.locators.YANDEX_LOGO)
    
    @allure.step("Проверить что открылся Яндекс")
    def check_ya_page(self):
        return self.find_element_with_wait(self.locators.YA_ELEMENT)  # Вернет элемент если найден
    
    @allure.step("Проверить что открылась главная Самоката")
    def check_scooter_page(self):
        return self.find_element_with_wait(self.locators.SCOOTER_ELEMENT).text