from .users.login import Login
from .users.registeration import Register
from .home_checks import check_scenario


def get_scenario():
    while True:
        try:
            return check_scenario(input("Enter r to register, l to login, x to exit: "))
        except AssertionError as error:
            print(error)


def start():
    print("--Welcome to the Fundraise Console App--")

    scenarios = {"r": Register, "l": Login, "x": quit}

    while True:
        try:
            scenario = get_scenario()
            scenarios[scenario]()
        except AssertionError as error:
            print(error)
