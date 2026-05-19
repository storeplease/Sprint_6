import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class Main_Page(BasePage):
    
    @allure.step("нажать на вопрос")
    def click_to_question(self, num):
        locator_formated = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(MainPageLocators.QUESTION_TO_SCROLL)
        self.click_to_element(locator_formated)

    @allure.step("получить текст ответа")
    def get_answer_text(self, num):
        locator_formated = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.find_element_with_wait(locator_formated).text
    
    @allure.step("проверить ответ")
    def check_answer(self, num, text_to_check):
        self.click_to_question(num)
        text = self.get_answer_text(num)
        return text == text_to_check
    
    @allure.step("принять куки")
    def accept_cookies(self):
        cookie_button = self.find_element_with_wait(MainPageLocators.COOKIE_BUTTON)
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)