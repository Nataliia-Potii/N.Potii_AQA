import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_up_page import SignUpPage


class User:
    """The User class created"""
    def __init__(self):
        """The constructor of the User class is created.
        The name and second_name were set with the default values of None"""
        self.name = None
        self.second_name = None

    def create(self):
        """The object method sets values to the name and second_name fields"""
        self.name = 'Nataliia'
        self.second_name = 'Potii'

    def remove(self):
        """The object method sets an empty str value to the name and second name fields"""
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    """The user fixture creates an object of the User class.
    Calls the object's create method.
    Returns the object after calling the object's create method in tests.
    After executing the test, it calls the object's remove method."""
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    """The fixture initializes an instance of a GitHub class.
    Returns the object after calling the object's create method in tests"""
    api = GitHub()

    yield api


@pytest.fixture
def database():
    """The fixture creates an instance of the Database class.
    Returns the object after calling the object's create method in tests"""
    database = Database()
    yield database


@pytest.fixture
def sign_in_page():
    """The fixture creates an instance of the SignInPage class.
    To call the method go_to to open the SignInPage.
    Returns the object after calling the object's create method in tests"""
    sign_in_page = SignInPage()
    sign_in_page.go_to()

    yield sign_in_page


@pytest.fixture
def sign_up_page():
    """The fixture creates an instance of the SignUpPage class.
    To call the method go_to to open the SignUpPage.
    Returns the object after calling the object's create method in tests"""
    sign_up_page = SignUpPage()
    sign_up_page.go_to()

    yield sign_up_page
