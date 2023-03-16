import pytest


@pytest.mark.check
def test_change_name(user):
    """The check that the name is 'Nataliia'."""
    assert user.name == 'Nataliia'


@pytest.mark.check
def test_change_second_name(user):
    """To check that the second name is 'Potii'."""
    assert user.second_name == 'Potii'
