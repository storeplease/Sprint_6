from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def find_text(self, locator, text):
        self.wait.until(
            EC.text_to_be_present_in_element(locator, text)
        )
        return self.driver.find_element(*locator).text
    
    def wait_until_element_disappears(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    def input_text(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def format_locators(self,locator_in, value):
        method, locator = locator_in
        locator = locator.format(value)
        return (method, locator)
    
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)   

    def switch_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        window_list = self.driver.window_handles
        self.driver.switch_to.window(window_list[-1])
