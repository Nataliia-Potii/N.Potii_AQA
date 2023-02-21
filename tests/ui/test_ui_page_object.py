import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object(sign_in_page):

    # виконуємо спробу увійти в систему Github
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
