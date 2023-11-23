import datetime

from .user_checks import (
    check_name,
    check_email,
    check_activate_email,
    check_password,
    check_phone,
)

from .user_utils import decrypt_password

class UserInputMixin:

    @staticmethod
    def get_user_id():
        current_time = datetime.datetime.now()
        user_id = int(current_time.timestamp())
        return str(user_id)

    @staticmethod
    def get_name(type="first"):
        while True:
            try:
                return check_name(input(f"May we have your {type} name please: "))
            except AssertionError as error:
                print(error)

    @staticmethod
    def get_email() -> str:
        while True:
            try:
                email = check_email(input("May we have your email please: "))
                check_activate_email(
                    input("If you want to activate your email, type: `please`: ")
                )
                return email
            except AssertionError as error:
                print(error)

    @staticmethod
    def get_password() -> str:
        while True:
            try:
                password = input("Please enter your password: ")
                confirm = input("Please confirm your password: ")
                check_password(password, confirm)
                return decrypt_password(password)
            except AssertionError as error:
                print(error)

    @staticmethod
    def get_phone() -> str:
        while True:
            try:
                return check_phone(input("May we have your phone, please: "))
            except AssertionError as error:
                print(error)


    




    

