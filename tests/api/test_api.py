import pytest


@pytest.mark.change
def test_remove_name(user):
    """
    The test changes the name to an empty string.
    To verify that the changes name field is empty as expected.
    """
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    """
    To check that the user name field has expected value - 'Nataliia'.
    """
    assert user.name == 'Nataliia'


@pytest.mark.check
def test_second_name(user):
    """
    To check that the user second name field has value - 'Potii'.
    """
    assert user.second_name == 'Potii'
