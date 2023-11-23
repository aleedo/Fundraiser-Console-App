from .user_inputs import UserInputMixin
from ..const import DATA_FILE_PATH
from ..utils import write_json
from .user_utils import get_registered_users
from .user import User
from typing import List


class Register(UserInputMixin):
    def __init__(self) -> None:
        self.registered_users = get_registered_users()
        self.user = self.create_user()
        self.add_user()

    def get_email(self) -> str:
        while True:
            try:
                email = super().get_email()
                self.check_registered(email)
                return email
            except AssertionError as error:
                print(error)

    def check_registered(self, email):
        assert not self.registered_users or email not in [
            user["email"] for user in self.registered_users.values()
        ], "Sorry, this email is already registered."

    def create_user(self):
        user_id = self.get_user_id()
        first_name = self.get_name()
        last_name = self.get_name("last")
        full_name = f"{first_name} {last_name}"
        email = self.get_email()
        password = self.get_password()
        phone = self.get_phone()

        return User(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            email=email,
            password=password,
            phone=phone,
            projects=[],
        )


    def add_user(self):
        self.registered_users[self.user.user_id] = self.user.user_info
        write_json(self.registered_users, DATA_FILE_PATH)
        print(f"Registered Succesfully with id: {self.user.user_id}")
