import datetime
from .project_checks import check_number, check_date, check_edit_project_choice


class ProjectInputMixin:
    @staticmethod
    def get_project_id():
        current_time = datetime.datetime.now()
        user_id = int(current_time.timestamp())
        return str(user_id)

    @staticmethod
    def get_title():
        return input("What is the title of the project: ")

    @staticmethod
    def get_details():
        return input("A small description for your project: ")

    @staticmethod
    def get_total_target():
        while True:
            try:
                return int(check_number(input("What is the total target to raise: ")))
            except AssertionError as error:
                print(error)

    @staticmethod
    def get_start_date() -> str:
        while True:
            try:
                start_date = check_date(
                    input("Enter the start date `d/m/y` of the campaign: ")
                )
                return start_date
            except AssertionError as error:
                print(error)

    @staticmethod
    def get_end_date() -> str:
        while True:
            try:
                end_date = check_date(
                    input("Enter the end date `d/m/y` of the campaign: ")
                )
                return end_date
            except AssertionError as error:
                print(error)

    @staticmethod
    def get_edit_choice():
        edit_choices = {
            "t": "title",
            "d": "details",
            "m": "total_target",
            "s": "start_date",
            "e": "end_date",
        }

        while True:
            try:
                choice = check_edit_project_choice(
                    input(
                        "Enter t for title, d for details, m for total target, s for start date, e for end date: "
                    )
                )

                edit_choice = edit_choices[choice]
                return edit_choice

            except AssertionError as error:
                print(error)
