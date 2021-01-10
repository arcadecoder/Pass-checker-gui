import requests
import hashlib


def request_api_data(query_char):
    """ requests data from an api and outputs a response"""
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check the API')
    return response


def pwned_api_check(password):
    """check password if it exists in api response
    Have to run our password through the sha1 algorithm
    """
    print(hashlib.sha1(password.encode('utf-8')))
    # sha1password = hashlib.sha1(password.encode('utf-8'))
