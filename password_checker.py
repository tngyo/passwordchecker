import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching : {response.status_code}, check api to run again')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if hash_to_check == h:
            return count
    return 0


def pawned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    res = request_api_data(first5)
    return get_password_leaks_count(res, tail)


def main(args):
    for check in args:
        count = pawned_api_check(check)
        if count:
            print(f'Password {check} has been leaked or hacked {count} number of times. Time to change?')
        else:
            print('{check} was NOT leaked. Good job, carry on!')
    return 'Program finished!'


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
