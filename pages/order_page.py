import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    
    @allure.step("Нажать кнопку Заказать вверху страницы")
    def click_order_button_top(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_TOP)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_TOP)
    
    @allure.step("Нажать кнопку Заказать внизу страницы")
    def click_order_button_bottom(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Заполнить поле Имя: {name}")
    def fill_name(self, name):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
    
    @allure.step("Заполнить поле Фамилия: {surname}")
    def fill_surname(self, surname):
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
    
    @allure.step("Заполнить поле Адрес: {address}")
    def fill_address(self, address):
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
    
    @allure.step("Выбрать станцию метро: {station}")
    def select_metro_station(self, station):
        self.click_to_element(OrderPageLocators.METRO_INPUT)
        locator_formated = self.format_locators(OrderPageLocators.METRO_STATION, station)
        self.scroll_to_element(locator_formated)
        self.click_to_element(locator_formated)
    
    @allure.step("Заполнить поле Телефон: {phone}")
    def fill_phone(self, phone):
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Заполнить поле Дата: {date}")
    def fill_date(self, date):
        self.input_text(OrderPageLocators.DATE_INPUT, date)
        self.click_to_element(OrderPageLocators.ORDER_HEADER)
    
    @allure.step("Выбрать срок аренды: {period}")
    def select_rental_period(self, period):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        locator_formated = self.format_locators(OrderPageLocators.RENTAL_OPTION, period)
        self.click_to_element(locator_formated)
    
    @allure.step("Заполнить поле Комментарий: {comment}")
    def fill_comment(self, comment):
        self.input_text(OrderPageLocators.COMMENT_INPUT, comment)
    
    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)
    
    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_MESSAGE).text
    
    @allure.step("Заполнить первую часть формы")
    def fill_first_form(self, name, surname, address, station, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station(station)
        self.fill_phone(phone)
        self.click_next_button()
    
    @allure.step("Заполнить вторую часть формы")
    def fill_second_form(self, date, period, color, comment=""):
        self.fill_date(date)
        self.select_rental_period(period)
        self.select_color(color)
        if comment:
            self.fill_comment(comment)
        self.click_order_button()
    
    @allure.step("Проверить, что заказ оформлен")
    def check_order_success(self):
        return "Заказ оформлен" in self.get_success_message()
    
    @allure.step("Закрыть всплывающее окно успешного заказа")
    def close_success_popup(self):
        self.click_to_element(OrderPageLocators.CHECK_STATUS_BUTTON)
    
    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click_to_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_to_element(OrderPageLocators.COLOR_GREY)