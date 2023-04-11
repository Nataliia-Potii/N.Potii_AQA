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

    def check_signup_form(self, email, firstname, lastname, password):
        """
        To find the cookie button and to click.
        To find the email field and to send the data.
        To find the firstname field and to send the data.
        To find the lastname field and to send the data.
        To find the password field and to send the data.
        To find the button and to click.
        """

        btn_cookie = self.driver.find_element(By.ID, "cookiebotDialogOkButton")
        btn_cookie.click()

        email_elem = self.driver.find_element(By.ID, 'email_id')
        email_elem.send_keys(email)

        first_elem = self.driver.find_element(By.ID, 'firstname_id')
        first_elem.send_keys(firstname)

        last_elem = self.driver.find_element(By.ID, 'lastname_id')
        last_elem.send_keys(lastname)

        pass_elem = self.driver.find_element(By.ID, 'password_id')
        pass_elem.send_keys(password)

        btn_elem = self.driver.find_element(By.XPATH, "/html/body/div[2]/section/div/div/div[2]/div/form/button")
        btn_elem.click()
        