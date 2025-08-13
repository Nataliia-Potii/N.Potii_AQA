import pytest


@pytest.mark.api
def test_user_exists(github_api):
    """
    The test created to check that user with this username exists on Github.
    """
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_non_exists(github_api):
    """
    The user does not exist on Github.
    """
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    """
    Repositories can be found on Github.
    """
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    """
    The repository doesn't exist on Github.
    """
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
