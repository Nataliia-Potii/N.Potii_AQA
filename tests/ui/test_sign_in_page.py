import pytest


@pytest.mark.ui
def test_check_correct_login_password(sign_in_page):
    """To check correct login and password.
    The user can log in."""
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("GitHub")


@pytest.mark.ui
def test_check_capital_letters_login(sign_in_page):
    """To check correct login written in capital letters and password.
    The user can log in."""
    sign_in_page.try_login("LORELEYSINGT@gmail.com")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("GitHub")


@pytest.mark.ui
def test_check_incorrect_login_password(sign_in_page):
    """The test with incorrect login and password. The user cannot log in."""
    sign_in_page.try_login("wrong@gmail.com")
    sign_in_page.try_password("wrong password")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_incorrect_login(sign_in_page):
    """The test with incorrect login. The user cannot log in."""
    sign_in_page.try_login("wrong@gmail.com", )
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_incorrect_password(sign_in_page):
    """The test with incorrect password. The user cannot log in."""
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("wrong password")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_empty_login_password(sign_in_page):
    """The test with empty login and password fields. The user cannot log in."""
    sign_in_page.try_login("")
    sign_in_page.try_password("")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_empty_password(sign_in_page):
    """The test with empty password field. The user cannot log in."""
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_empty_login(sign_in_page):
    """The test with empty login field. The user cannot log in."""
    sign_in_page.try_login("")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_spaces_login(sign_in_page):
    """The test with spaces in login field. The user cannot log in."""
    sign_in_page.try_login("  loreleysingt@gmail.com  ")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_capital_letters_password(sign_in_page):
    """The test with password written with capital letters. The user cannot log in."""
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("020202NM")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_symbols_login(sign_in_page):
    """The test with symbols in login field. The user cannot log in."""
    sign_in_page.try_login("«»‘~!@#$%^&*()?>[ /*<!—«», «${code}»;—>")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

@pytest.mark.ui
def test_check_cyrillic_login(sign_in_page):
    """The test with cyrillic letters in login field. The user cannot log in."""
    sign_in_page.try_login("дщкудуніштпе@gmail.com")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
