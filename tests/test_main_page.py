import allure
import pytest

from data import answers_data
from pages import main_page
from urls import BASE_URL
from pages.main_page import Main_Page

class TestQuestions:

    @allure.title("Проверка ответа на вопрос {num}")
    @allure.description("Ожидаемый текст: {expected_text}")
    @pytest.mark.parametrize("num, expected_text", answers_data.items())
    def test_question_and_answer(self, driver, num, expected_text):
        main_page = Main_Page(driver)
        main_page.go_to_url(BASE_URL)
        main_page.accept_cookies()
        main_page.click_to_question(num)
        actual_text = main_page.get_answer_text(num)
        assert actual_text == expected_text, (
            f"Ответ на вопрос {num} не совпадает c ожидаемым.\n"
            f"Ожидаемый: {expected_text}\n"
            f"Полученный: {actual_text}"
        )