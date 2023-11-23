import pytest
from unittest.mock import patch
from ..users.registeration import Register, User
from ..const import DATA_FILE_PATH


@pytest.fixture
def user_info():
    return {
        "user_id": "1700501850",
        "first_name": "Test",
        "last_name": "Test",
        "full_name": "Test Test",
        "email": "test@example.com",
        "password": "e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178",
        "phone": "01000000000",
        "projects": [],
    }


@pytest.fixture
def user(user_info):
    return User(**user_info)


@pytest.fixture
def mock_user_id(user, mocker):
    return mocker.patch(
        "app.users.registeration.Register.get_user_id", return_value=user.user_id
    )


@pytest.fixture
def mock_user_get_name(user, mocker):
    return mocker.patch(
        "app.users.registeration.Register.get_name", return_value=user.first_name
    )


@pytest.fixture
def mock_user_get_email(user, mocker):
    return mocker.patch(
        "app.users.registeration.Register.get_email", return_value=user.email
    )


@pytest.fixture
def mock_user_get_password(user, mocker):
    return mocker.patch(
        "app.users.registeration.Register.get_password", return_value=user.password
    )


@pytest.fixture
def mock_user_get_phone(user, mocker):
    return mocker.patch(
        "app.users.registeration.Register.get_phone", return_value=user.phone
    )


@patch("app.users.registeration.write_json")
def test_create_user(
    mock_write_json,
    mock_user_id,
    mock_user_get_name,
    mock_user_get_email,
    mock_user_get_password,
    mock_user_get_phone,
    user,
):
    register_instance = Register()

    assert mock_user_id.call_count == 1
    assert mock_user_get_name.call_count == 2
    assert mock_user_get_email.call_count == 1
    assert mock_user_get_password.call_count == 1
    assert mock_user_get_phone.call_count == 1
    assert register_instance.user == user


def test_add_user(
    user,
    mocker,
):
    mocker.patch("app.users.registeration.Register.create_user", return_value=user)
    mock_write_json = mocker.patch("app.users.registeration.write_json")

    register_instance = Register()

    assert user.user_id in register_instance.registered_users

    mock_write_json.assert_called_once_with(
        register_instance.registered_users, DATA_FILE_PATH
    )
