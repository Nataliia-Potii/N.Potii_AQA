import pytest

# Tests were created for testing:
# The user can log into an account with a valid login and password.
# The user cannot log into an account with an invalid login and password.
# The error message is appearing after entering an invalid login and password.
# The links (Forgot password, Create an account, Terms, Privacy,
# Security, Contact GitHub) are working as expected.


@pytest.mark.ui
def test_check_correct_login_password(sign_in_page):
    """
    To check correct login and password.
    The user can log in.
    """
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("GitHub")


@pytest.mark.ui
def test_check_capital_letters_login(sign_in_page):
    """
    To check correct login written in capital letters and password.
    The user can log in.
    """
    sign_in_page.try_login("LORELEYSINGT@gmail.com")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("GitHub")


@pytest.mark.ui
def test_check_incorrect_login_password(sign_in_page):
    """
    The test with incorrect login and password. The user cannot log in.
    """
    sign_in_page.try_login("wrong@gmail.com")
    sign_in_page.try_password("wrong password")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_incorrect_login(sign_in_page):
    """
    The test with incorrect login. The user cannot log in.
    """
    sign_in_page.try_login("wrong@gmail.com", )
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_incorrect_password(sign_in_page):
    """
    The test with incorrect password. The user cannot log in.
    """
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("wrong password")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_empty_login_password(sign_in_page):
    """
    The test with empty login and password fields. The user cannot log in.
    """
    sign_in_page.try_login("")
    sign_in_page.try_password("")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_empty_password(sign_in_page):
    """
    The test with empty password field. The user cannot log in.
    """
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_empty_login(sign_in_page):
    """
    The test with empty login field. The user cannot log in.
    """
    sign_in_page.try_login("")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_spaces_login(sign_in_page):
    """
    The test with spaces in login field. The user cannot log in.
    """
    sign_in_page.try_login("  loreleysingt@gmail.com  ")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_capital_letters_password(sign_in_page):
    """
    The test with password written with capital letters. The user cannot login.
    """
    sign_in_page.try_login("loreleysingt@gmail.com")
    sign_in_page.try_password("020202NM")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_symbols_login(sign_in_page):
    """
    The test with symbols in login field. The user cannot log in.
    """
    sign_in_page.try_login("«»‘~!@#$%^&*()?>[ /*<!—«», «${code}»;—>")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_cyrillic_login(sign_in_page):
    """
    The test with cyrillic letters in login field. The user cannot log in.
    """
    sign_in_page.try_login("дщкудуніштпе@gmail.com")
    sign_in_page.try_password("020202nm")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")


@pytest.mark.ui
def test_check_error_message(sign_in_page):
    """
    To check that after entering the wrong login and password 
    the error message is appering and it is as expected.
    """
    sign_in_page.try_login("wrong@gmail.com")
    sign_in_page.try_password("wrong")
    sign_in_page.click_signin_button()

    assert sign_in_page.check_error_message("Incorrect username or password.")


@pytest.mark.ui
def test_forgot_password_link(sign_in_page):
    """
    To check that the forgot password link works and the correct page is opened.
    """
    sign_in_page.click_forgot_password()

    assert sign_in_page.check_title("Forgot your password? · GitHub")


@pytest.mark.ui
def test_create_account_link(sign_in_page):
    """
    To check that the create account link works and the correct page is opened.
    """
    sign_in_page.click_create_account()

    assert sign_in_page.check_title("Join GitHub · GitHub")


@pytest.mark.ui
def test_terms_link(sign_in_page):
    """
    To check that the terms link works and the correct page is opened.
    """
    sign_in_page.click_terms()

    assert sign_in_page.check_title("GitHub Terms of Service - GitHub Docs")


@pytest.mark.ui
def test_privacy_link(sign_in_page):
    """
    To check that the privacy link works and the correct page is opened.
    """
    sign_in_page.click_privacy()

    assert sign_in_page.check_title("GitHub Privacy Statement - GitHub Docs")


@pytest.mark.ui
def test_security_link(sign_in_page):
    """
    To check that the security link works and the correct page is opened.
    """
    sign_in_page.click_security()

    assert sign_in_page.check_title("GitHub Security · GitHub")


@pytest.mark.ui
def test_contact_link(sign_in_page):
    """
    To check that the contact GitHub link works and the correct page is opened.
    """
    sign_in_page.click_contact()

    assert sign_in_page.check_title("GitHub Support")
