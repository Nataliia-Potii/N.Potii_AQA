import pytest

# The testing that the user cannot create an account with invalid data on Reserved.com.


@pytest.mark.ui_up
def test_check_empty_fields(sign_up_page):
    """
    The test with empty fields.
    """
    sign_up_page.check_signup_form("", "", "", "")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_registered_email(sign_up_page):
    """
    The test with registered email.
    """
    sign_up_page.check_signup_form("natatest@gmail.com", "N", "N", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_cyrillic_email(sign_up_page):
    """
    The test with cyrillic email.
    """
    sign_up_page.check_signup_form("тест@gmail.com", "N", "N", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_incorrect_email(sign_up_page):
    """
    The test with incomplete email.
    """
    sign_up_page.check_signup_form("@gmail.com", "N", "N", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_symbols_email(sign_up_page):
    """
    To check the email with invalid symbols.
    """
    sign_up_page.check_signup_form("!!!##@^^^.**$", "N", "N", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_too_short_password(sign_up_page):
    """
    The test with too short password (5 characters).
    """
    sign_up_page.check_signup_form("nata3.test@gmail.com", "N", "N", "11111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_incorrect_first_name(sign_up_page):
    """
    The test with digit in first name field.
    """
    sign_up_page.check_signup_form("nata3.test@gmail.com", "1", "N", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_incorrect_last_name(sign_up_page):
    """
    The test with digit in last name field.
    """
    sign_up_page.check_signup_form("nata3.test@gmail.com", "N", "1", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_too_long_first_name(sign_up_page):
    """
    The test with too long first name (31 characters).
    """
    sign_up_page.check_signup_form(
        "nata3.test@gmail.com", "Nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", "N", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")


@pytest.mark.ui_up
def test_check_too_long_last_name(sign_up_page):
    """
    The test with too long last name (31 characters).
    """
    sign_up_page.check_signup_form(
        "nata3.test@gmail.com", "N", "Nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn", "111111")

    assert sign_up_page.check_title("Reserved.com - купуйте онлайн")
