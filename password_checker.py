import requests
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching : {response.status_code}, check api to run again')
    return response


def read_response(response):
    print(response.text)


def pawned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first5)
    read_response(res)


# hashed = pawned_api_check("password123")
# print(request_api_data(hashed))
pawned_api_check("password124")
