from .user_checks import check_email
from .user_utils import decrypt_password, get_registered_users
from .user import User
from .user_profile import Profile


class Login:
    def __init__(self) -> None:
        self.registered_users = get_registered_users()
        user_id = self.login()
        Profile(User(**self.registered_users[user_id]))


    def login(self):
        while True:
            print("-----------------------------------------------")
            print("--------Welcome to the login page--------------")

            email, password = self.get_user_data()

            for user_id, user_info in self.registered_users.items():
                if user_info["email"] == email and user_info["password"] == password:
                    return user_id

            print("Sorry email or password is not right")

    def get_user_data(self):
        while True:
            try:
                email = check_email(input("Enter your email please: "))
                password = decrypt_password(input("Enter your password please: "))
                return email, password
            except AssertionError as error:
                print(error)
