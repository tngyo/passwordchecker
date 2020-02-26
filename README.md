# passwordchecker for breaches

This python file runs a check for password(s) supplied as parameter/s after python3 filename is called.
For example, to check if 'password123' has been found before and how many times, run the file as follows:

$python3 password_checker.py password123

The api is from https://haveibeenpwned.com/API/v3#BreachesForAccount

You will need to have Python3 installed.

The check is safe in the sense that it uses k-anonimty. Program hashed password locally and 
send only first 5 hasehed characters, received the rest with matching prefixes, before matching
again the suffixes with the rest of the local hashed password queried. That means no comeplete text (unencrypted)
password was sent over the internet to be checked.

![password checker](https://github.com/palden/passwordchecker/blob/master/password_checker.png)
