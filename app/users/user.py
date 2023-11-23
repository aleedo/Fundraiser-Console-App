from typing import List
from dataclasses import dataclass, asdict
from ..const import DATA_FILE_PATH
from ..projects.project import ProjectFactory
from .user_utils import get_registered_users
from ..utils import write_json


@dataclass
class User:
    user_id: str
    first_name: str
    last_name: str
    full_name: str
    email: str
    password: str
    phone: str
    projects: List[str]

    @property
    def user_info(self) -> dict:
        return asdict(self)

    def __post_init__(self):
        object.__setattr__(self, "registered_users", get_registered_users())

    def get_project_id(self) -> str:
        while True:
            try:
                project_id = self.check_project(input("Enter the project id: "))
                return project_id
            except AssertionError as error:
                print(error)

    def check_project(self, project_id: str) -> str:
        assert project_id in self.projects, "You don't have projects with this id"
        return project_id

    def create_project(self) -> None:
        ProjectFactory(self).create_project()

        self.registered_users[self.user_id]["projects"] = self.projects
        write_json(self.registered_users, DATA_FILE_PATH)

    def view_project(self) -> None:
        project_id = self.get_project_id()
        ProjectFactory(self).view_project(project_id)

    def edit_project(self) -> None:
        project_id = self.get_project_id()
        ProjectFactory(self).edit_project(project_id)

        self.registered_users[self.user_id]["projects"] = self.projects
        write_json(self.registered_users, DATA_FILE_PATH)

    def delete_project(self) -> None:
        project_id = self.get_project_id()
        ProjectFactory(self).delete_project(project_id)

        self.registered_users[self.user_id]["projects"] = self.projects

        write_json(self.registered_users, DATA_FILE_PATH)

    def search_projects(self) -> None:
        ProjectFactory(self).search_projects()

    def delete_account(self) -> None:
        user_projects = self.projects.copy()
        for project_id in user_projects:
            ProjectFactory(self).delete_project(project_id)

        del self.registered_users[self.user_id]
        write_json(self.registered_users, DATA_FILE_PATH)
        del self

        print("Your Account Has Been Deleted Successfully")
        quit()
