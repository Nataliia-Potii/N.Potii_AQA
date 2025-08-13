from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class SignInPage(BasePage):
    """
    Created SignInPage class is inherited from the BasePage class.
    """
    URL = 'https://github.com/login'

    def init(self, driver):
        """
        Calling the constructor of the parent class.
        """
        super().__init__(driver)

    def go_to(self):
        """
        The go_to method was created to open the page.
        """
        self.driver.get(SignInPage.URL)

    def try_login(self, username):
        """
        To find the login field and send the data.
        """
        login_elem = self.driver.find_element(By.ID, 'login_field')
        login_elem.send_keys(username)

    def try_password(self, password):
        """
        To find the password field and send the data.
        """  
        pass_elem = self.driver.find_element(By.ID, 'password')
        pass_elem.send_keys(password)

    def click_signin_button(self):
        """
        To find the button and click it.
        """
        btn_elem = self.driver.find_element(By.NAME, "commit")
        btn_elem.click()

    def check_error_message(self, expected_message):
        """
        To find an error message and to compere it with the expected one.
        """
        error_elem = self.driver.find_element(By.CLASS_NAME, "js-flash-alert")
        
        return error_elem.text == expected_message
    
    def click_forgot_password(self):
        """
        To find the forgot password link and click it.
        """
        forgot_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[4]/form/div/a")
        forgot_link.click()

    def click_create_account(self):
        """
        To find the create_account link and click it.
        """
        account_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/p/a")
        account_link.click()
        time.sleep(1)

    def click_terms(self):
        """
        To find the terms link and click it.
        """
        terms_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/ul/li[1]/a")
        terms_link.click()

    def click_privacy(self):
        """
        To find the privacy link and click it.
        """
        privacy_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/ul/li[2]/a")
        privacy_link.click()

    def click_data(self):
        """
        To find the security link and click it.
        """
        security_link = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/ul/li[3]/a")
        security_link.click()

    def click_contact(self):
        """
        To find the contact GitHub link and click it.
        """
        contact_link = self.driver.find_element(By.CLASS_NAME, "Link--secondary")
        contact_link.click()
