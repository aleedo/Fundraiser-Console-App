import re


def check_name(s):
    assert s.isalpha() and s, "Sorry not a valid name"
    return s.title()


def check_email(email):
    assert re.match(
        "[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.[a-zA-Z]+", email
    ), "Sorry not a valid email"
    return email.lower()


def check_activate_email(s):
    assert re.match(r"^please$", s, re.I), "Failed to activate your email"


def check_password(password, confirm):
    assert (
        password and confirm and password == confirm
    ), "Sorry Passwords are not identical or can't be left empty"
    return password, confirm


def check_phone(phone):
    assert re.match("^01\d{9}$", phone), "Sorry not a valid phone"
    return phone


def check_project_choice(s):
    assert re.match(
        r"^[cedsqvx]$", s, re.I
    ), "Sorry, Please choose one of `c`, `e`, `d`, `s`, `q`, `v`, `x`"
    return s



