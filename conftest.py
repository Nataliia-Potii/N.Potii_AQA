import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page import SignInPage


class User:

    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Nataliia'
        self.second_name = 'Potii'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api


@pytest.fixture
def database():
    database = Database()
    yield database


@pytest.fixture
def sign_in_page():
    # створюємо обєкт сторінки
    sign_in_page = SignInPage()
    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # закриваємо браузер
    yield sign_in_page
