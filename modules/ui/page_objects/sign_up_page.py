from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):
    """
    The SignUpPage class is inherited from the BasePage class.
    """
    URL = 'https://www.reserved.com/ua/uk/customer/account/login/#register'

    def __init__(self):
        """
        Calling the constructor of the parent class.
        """
        super().__init__()

    def go_to(self):
        """
        To open the page - https://www.reserved.com/ua/uk/customer/account/login/#register.
        """
        self.driver.get(SignUpPage.URL)

    def click_cookie(self):
        """
        To find the cookie button and to click.
        """
        btn_cookie = self.driver.find_element(By.ID, "cookiebotDialogOkButton")
        btn_cookie.click()

    def check_email(self, email):
        """
        To find the email field and to send the data.
        """
        email_elem = self.driver.find_element(By.ID, 'email_id')
        email_elem.send_keys(email)

    def check_firstname(self, firstname):
        """
        To find the firstname field and to send the data.
        """
        first_elem = self.driver.find_element(By.ID, 'firstname_id')
        first_elem.send_keys(firstname)

    def check_lastname(self, lastname):
        """
        To find the lastname field and to send the data.
        """
        last_elem = self.driver.find_element(By.ID, 'lastname_id')      
        last_elem.send_keys(lastname)

    def check_password(self, password):
        """
        To find the password field and to send the data.
        """
        pass_elem = self.driver.find_element(By.ID, 'password_id')
        pass_elem.send_keys(password)

    def click_btn(self):
        """
        To find the button and to click.
        """
        btn_elem = self.driver.find_element(By.XPATH, "/html/body/div[2]/section/div/div/div[2]/div/form/button")
        btn_elem.click()

    def check_title(self, expected_title):
        """
        To check if the page header matches what is expected.
        """
        return self.driver.title == expected_title

