import pytest
import requests


@pytest.mark.http
def test_first_request():
    """The test sends an HTTP request (the GET method) to the address of a server.
    It stores the response in a variable.
    The test displays the server response using f-strings."""
    r = requests.get('https://api.github.com/zen')
    print((f"Response is {r.text}").encode("utf-8"))


@ pytest.mark.http
def test_second_request():
    """The test sends an HTTP request (the GET method) to the address.
    To check that the name attribute in response is 'Chris Wanstrath'.
    To check that the status code of the response is 200
    To check that the server header of the response is 'GitHub.com'."""
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@ pytest.mark.http
def test_status_code_request():
    """The test sends an HTTP request (the GET method) to the address.
    To check that the status code of the response is 404"""
    r = requests.get('https://api.github.com/users/Nataliia_Potii')

    assert r.status_code == 404
