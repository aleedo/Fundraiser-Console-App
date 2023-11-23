import os
from .user_checks import check_project_choice


class Profile:
    def __init__(self, user) -> None:
        self.profile_options(user)

    def profile_options(self, user):
        os.system("clear")

        while True:
            print("Welcome to your profile")
            profile_choices = {
                "c": user.create_project,
                "e": user.edit_project,
                "v": user.view_project,
                "d": user.delete_project,
                "s": user.search_projects,
                "q": user.delete_account,
                "x": quit,
            }

            try:
                choice = check_project_choice(
                    input(
                        "Enter c to create a project, e to edit, v to view, d to delete, s to search, q to delete account, x to exit: "
                    )
                )
                profile_choices[choice]()

            except AssertionError as error:
                print(error)
