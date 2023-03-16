import requests


class GitHub:
    """The class describes the client API which allows to work with GitHub"""
    def get_user(self, username):
        """The method send request get using parameter username to find an user"""
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        """The method send request get using parameter name to search repositories"""
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name},
        )
        body = r.json()

        return body
