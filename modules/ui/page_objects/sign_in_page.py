from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    """The SignInPage class is inherited from the BasePage class."""
    URL = 'https://github.com/login'

    def __init__(self):
        """Calling the constructor of the parent class."""
        super().__init__()

    def go_to(self):
        """To open the page."""
        self.driver.get(SignInPage.URL)

    def try_login(self, username):
        """To find the login field and send the data."""
        login_elem = self.driver.find_element(By.ID, 'login_field')
        login_elem.send_keys(username)

    def try_password(self, password):
        """To find the password field and send the data."""  
        pass_elem = self.driver.find_element(By.ID, 'password')
        pass_elem.send_keys(password)

    def click_button(self):
        """To find the button and to click."""
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

    def check_title(self, expected_title):
        """To check if the page header matches what is expected."""
        return self.driver.title == expected_title
