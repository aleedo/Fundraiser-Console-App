import json
from dateutil import parser
from dataclasses import dataclass, asdict
from .project_checks import check_start_end_date
from .project_inputs import ProjectInputMixin
from .project_utils import get_all_projects
from ..const import PROJECT_FILE_PATH
from ..utils import write_json


@dataclass
class Project:
    project_id: str
    user_id: str
    title: str
    details: str
    total_target: int
    start_date: str
    end_date: str

    @property
    def project_info(self):
        return asdict(self)


class ProjectFactory(ProjectInputMixin):
    def __init__(self, user) -> None:
        self.user = user
        self.all_projects = get_all_projects()

    def create_project(self):
        project_id = self.get_project_id()
        user_id = self.user.user_id
        title = self.get_title()
        details = self.get_details()
        total_target = self.get_total_target()
        start_date = self.get_start_date()
        end_date = self.get_end_date(start_date)

        self.project = Project(
            project_id=project_id,
            user_id=user_id,
            title=title,
            details=details,
            total_target=total_target,
            start_date=start_date,
            end_date=end_date,
        )

        self.user.projects.append(self.project.project_id)
        self.all_projects[self.project.project_id] = self.project.project_info
        write_json(self.all_projects, PROJECT_FILE_PATH)
        print(
            f"Project has been created by {self.user.full_name}, Thank you. project id = {self.project.project_id}"
        )

    def get_start_date(self) -> str:
        while True:
            try:
                start_date = super().get_start_date()

                if hasattr(self, "project"):
                    check_start_end_date(start_date, self.project.end_date)

                return start_date
            except AssertionError as error:
                print(error)

    def get_end_date(self, __start_date=None) -> str:
        while True:
            try:
                end_date = super().get_end_date()
                check_start_end_date(
                    __start_date if __start_date else self.project.start_date, end_date
                )
                return end_date
            except AssertionError as error:
                print(error)

    def view_project(self, project_id):
        project = self.all_projects[project_id]
        print(f"About the project:\n{json.dumps(project, indent=4)}")

    def edit_project(self, project_id):
        project_info = self.all_projects[project_id]
        self.project = Project(**project_info)

        edit_choice = self.get_edit_choice()
        setattr(self.project, edit_choice, getattr(self, f"get_{edit_choice}")())

        self.all_projects[project_id] = self.project.project_info
        write_json(self.all_projects, PROJECT_FILE_PATH)
        print(f"Project has been edited successfully.")

    def delete_project(self, project_id):
        self.user.projects.remove(project_id)
        del self.all_projects[project_id]
        write_json(self.all_projects, PROJECT_FILE_PATH)
        print(f"Project has been deleted successfully.")

    def search_projects(self):
        start_date = self.get_start_date()

        filtered_projects = list(
            filter(
                lambda project_info: parser.parse(Project(**project_info).start_date)
                == parser.parse(start_date),
                self.all_projects.values(),
            )
        )
        print(f"Projects: {json.dumps(filtered_projects, indent=4)}")
