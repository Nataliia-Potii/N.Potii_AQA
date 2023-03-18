from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    """
    The class BasePage contains basic operations for working with the browser.
    The Path class attribute is the way to the root project.
    The Driver_name class attribute specifies the driver name.
    """
    PATH = r"C:\Users\lorel\N.Potii_AQA"
    DRIVER_NAME = "chromedriver"

    def __init__(self):
        """
        An object for communication with the webdriver is initialized in the constructor.
        """
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )

    def close(self):
        """
        The object's method closes the open browser.
        """
        self.driver.close()

    def check_title(self, expected_title):
        """
        To check if the page header matches what is expected.
        """
        return self.driver.title == expected_title
