import pytest
from unittest.mock import patch
from ..users.user import User
from ..projects.project import Project
from ..const import DATA_FILE_PATH


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
def user(user_info):
    return User(**user_info)


@pytest.fixture
def project(project_info):
    return Project(**project_info)


def test_get_project_id(mocker, user):
    mocker.patch("builtins.input", return_value="1700510972")
    project_id = user.get_project_id()
    assert project_id == "1700510972"


@pytest.fixture
def mock_create_project(mocker, project):
    return mocker.patch(
        "app.projects.project.ProjectFactory.create_project",
        return_value=project,
    )


@pytest.fixture
def mock_write_json(mocker):
    return mocker.patch("app.users.user.write_json")


def test_create_project(mocker, mock_write_json, mock_create_project, user, project):
    with patch.object(user, "registered_users", {user.user_id: user.user_info}):
        user.create_project()
        assert project.project_id in user.projects
        mock_write_json.assert_called_once_with(user.registered_users, DATA_FILE_PATH)


@patch("app.projects.project.ProjectFactory.view_project")
def test_view_project(mock_view_project, mocker, user):
    with patch.object(user, "registered_users", {user.user_id: user.user_info}):
        mocker.patch("builtins.input", return_value="1700510972")
        user.view_project()
        mock_view_project.assert_called_once_with(user.get_project_id())


@patch("app.projects.project.ProjectFactory.edit_project")
def test_edit_project(mock_edit_project, mock_write_json, mocker, user):
    with patch.object(user, "registered_users", {user.user_id: user.user_info}):
        mocker.patch("builtins.input", return_value="1700510972")
        user.edit_project()
        assert user.user_id in user.registered_users
        mock_edit_project.assert_called_once_with(user.get_project_id())
        mock_write_json.assert_called_once_with(user.registered_users, DATA_FILE_PATH)


@patch("app.projects.project.ProjectFactory.delete_project")
def test_delete_project(mock_delete_project, mock_write_json, mocker, user, project):
    with patch.object(user, "registered_users", {user.user_id: user.user_info}):
        mocker.patch("builtins.input", return_value="1700510972")
        user.delete_project()
        assert user.user_id in user.registered_users
        mock_delete_project.assert_called_once_with(user.get_project_id())
        mock_write_json.assert_called_once_with(user.registered_users, DATA_FILE_PATH)


@patch("app.projects.project.ProjectFactory.search_projects")
def test_search_projects(mock_search_projects, user):
    user.search_projects()

    mock_search_projects.assert_called_once()
