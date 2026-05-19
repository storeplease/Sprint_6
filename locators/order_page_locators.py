from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Кнопки заказа
    ORDER_BUTTON_TOP = By.XPATH, '//div[contains(@class, "Header")]//button[text()="Заказать"]'
    ORDER_BUTTON_BOTTOM = By.XPATH, '//div[contains(@class, "Home")]//button[text()="Заказать"]'
    
    # Форма заказа
    NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_INPUT = By.XPATH, '//input[@placeholder="* Станция метро"]'
    METRO_STATION = By.XPATH, '//div[text()="{}"]'  # Для выбора станции
    PHONE_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'
    
    # Вторая часть формы
    ORDER_HEADER = By.XPATH, '//div[text()="Про аренду"]'
    DATE_INPUT = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD = By.XPATH, '//div[text()="* Срок аренды"]'
    RENTAL_OPTION = By.XPATH, '//div[text()="{}"]'  # Для выбора срока
    ORDER_TITLE = By.XPATH, '//div[contains(@class, "Order_Title")]'
    COLOR_BLACK = By.XPATH, '//label[@for="black"]'
    COLOR_GREY = By.XPATH, '//label[@for="grey"]'
    COMMENT_INPUT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Order_Buttons")]//button[text()="Заказать"]'
    
    # Подтверждение заказа
    CONFIRM_BUTTON = By.XPATH, '//button[text()="Да"]'
    SUCCESS_MESSAGE = By.XPATH, '//div[text()="Заказ оформлен"]'
    CHECK_STATUS_BUTTON = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Посмотреть статус"]'
    
    # Логотипы
    SCOOTER_LOGO = By.XPATH, '//a[@href="/"]'
    YANDEX_LOGO = By.XPATH, '//a[@href="//yandex.ru"]'