import pytest
import datetime
from unittest.mock import patch
from ..projects.project import ProjectFactory, Project
from ..users.user import User
from ..const import PROJECT_FILE_PATH


@pytest.fixture
def user_info():
    return {
        "user_id": "1700611829",
        "first_name": "Test",
        "last_name": "User",
        "full_name": "Test User",
        "email": "test@example.com",
        "password": "test_password",
        "phone": "01000000000",
        "projects": ["1700510972"],
    }


@pytest.fixture
def user(user_info):
    return User(**user_info)


@pytest.fixture
def current_date():
    # Only can from next day
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")


@pytest.fixture
def future_date():
    return (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%d/%m/%Y")


@pytest.fixture
def project_info():
    return {
        "project_id": "1700510972",
        "user_id": "1700611829",
        "title": "ok",
        "details": "ok",
        "total_target": 1,
        "start_date": "1/1/2025",
        "end_date": "1/1/2027",
    }


@pytest.fixture
def project(project_info):
    return Project(**project_info)


@pytest.fixture
def mock_write_json(mocker):
    return mocker.patch("app.projects.project.write_json")


@pytest.fixture
def mock_get_all_projects(mocker, project):
    return mocker.patch(
        "app.projects.project.get_all_projects",
        return_value={project.project_id: project.project_info},
    )


def test_create_project(
    mock_get_all_projects,
    mock_write_json,
    mocker,
    user,
    project,
    current_date,
    future_date,
):
    input_values = [
        project.project_id,
        "Title",
        "Details",
        "1",
        current_date,
        future_date,
    ]

    with patch.object(user, "projects", [project.project_id]):
        mocker.patch("builtins.input", side_effect=input_values)
        ProjectFactory(user).create_project()
        assert project.project_id in user.projects
        assert project.project_id in ProjectFactory(user).all_projects
        mock_write_json.assert_called_once_with(
            ProjectFactory(user).all_projects, PROJECT_FILE_PATH
        )


def test_view_project(mock_get_all_projects, user, project, mocker):
    with patch.object(user, "projects", [project.project_id]):
        mocker.patch("builtins.input", return_value=project.project_id)
        ProjectFactory(user).view_project(project.project_id)
        assert project.project_id in user.projects
        assert project.project_id in ProjectFactory(user).all_projects


def test_delete_project(mock_get_all_projects, mock_write_json, mocker, user, project):
    with patch.object(user, "projects", [project.project_id]):
        mocker.patch("builtins.input", return_value=project.project_id)
        ProjectFactory(user).delete_project(project.project_id)
        assert project.project_id not in user.projects
        assert project.project_id not in ProjectFactory(user).all_projects
        mock_write_json.assert_called_once_with(
            ProjectFactory(user).all_projects, PROJECT_FILE_PATH
        )


@pytest.mark.parametrize(
    "edit_choice, new_value, attribute_name",
    [
        ("t", "New Title", "title"),
        ("d", "New Details", "details"),
    ],
    ids=["edit_title", "edit_details"],
)
def test_edit_project_parametrized(
    mock_get_all_projects,
    mock_write_json,
    mocker,
    user,
    project,
    edit_choice,
    new_value,
    attribute_name,
):
    mocker.patch(
        "builtins.input", side_effect=[project.project_id, edit_choice, new_value]
    )

    with patch.object(user, "projects", [project.project_id]):
        ProjectFactory(user).edit_project(project.project_id)

        assert (
            ProjectFactory(user).all_projects[project.project_id][attribute_name]
            == new_value
        )
        mock_write_json.assert_called_once_with(
            ProjectFactory(user).all_projects, PROJECT_FILE_PATH
        )


def test_search_projects(mock_get_all_projects, mocker, user, project, current_date):
    mocker.patch("builtins.input", return_value=current_date)
    mocker.patch.object(
        ProjectFactory(user),
        "all_projects",
        {project.project_id: project.project_info},
    )
    mocker.patch("builtins.print")
    ProjectFactory(user).search_projects()
