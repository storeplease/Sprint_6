# tests/test_order_page.py
import allure
from data import order_data
from urls import BASE_URL
from pages.main_page import Main_Page
from pages.order_page import OrderPage
from pages.external_navigation import ExternalNavigation


class TestOrderPage:
    
    @allure.title("Позитивный сценарий заказа - кнопка вверху")
    @allure.description("Проверка заказа через кнопку вверху страницы")
    def test_order_scooter_top_button(self, driver):
        main_page = Main_Page(driver)
        main_page.go_to_url(BASE_URL)
        main_page.accept_cookies()
        
        order_page = OrderPage(driver)
        order_page.click_order_button_top()
        
        order_page.fill_first_form(
            order_data[0]["name"],
            order_data[0]["surname"],
            order_data[0]["address"],
            order_data[0]["station"],
            order_data[0]["phone"]
        )
        order_page.fill_second_form(
            order_data[0]["date"],
            order_data[0]["period"],
            order_data[0]["color"],
            order_data[0]["comment"]
        )
        order_page.confirm_order()
        
        assert order_page.check_order_success(), "Заказ не оформлен"
    
    @allure.title("Позитивный сценарий заказа - кнопка внизу")
    @allure.description("Проверка заказа через кнопку внизу страницы")
    def test_order_scooter_bottom_button(self, driver):
        main_page = Main_Page(driver)
        main_page.go_to_url(BASE_URL)
        main_page.accept_cookies()
        
        order_page = OrderPage(driver)
        order_page.click_order_button_bottom()
        
        order_page.fill_first_form(
            order_data[1]["name"],
            order_data[1]["surname"],
            order_data[1]["address"],
            order_data[1]["station"],
            order_data[1]["phone"]
        )
        order_page.fill_second_form(
            order_data[1]["date"],
            order_data[1]["period"],
            order_data[1]["color"],
            order_data[1]["comment"]
        )
        order_page.confirm_order()
        assert order_page.check_order_success(), "Заказ не оформлен"
    
    @allure.title("Проверка перехода на главную по логотипу Самоката")
    @allure.description("Клик на логотип Самоката ведет на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        main_page = Main_Page(driver)
        main_page.go_to_url(BASE_URL)
        main_page.accept_cookies()

        order_page = OrderPage(driver)
        order_page.click_order_button_top()
    
        nav = ExternalNavigation(driver)
        nav.click_scooter_logo()
        assert "Самокат" in nav.check_scooter_page(), "Не перешли на главную"
    
    @allure.title("Проверка перехода на Яндекс по логотипу")
    @allure.description("Клик на логотип Яндекса открывает Яндекс в новом окне")
    def test_yandex_logo_navigation(self, driver):
        main_page = Main_Page(driver)
        main_page.go_to_url(BASE_URL)
        main_page.accept_cookies()
        
        nav = ExternalNavigation(driver)
        nav.click_yandex_logo()
        nav.switch_window()
        assert nav.check_ya_page(), "Не перешли на Яндекс"