import pytest
import datetime
from ..projects.project_checks import *
from ..home_checks import *
from ..users.user_checks import *


@pytest.mark.parametrize(
    "input_name, expected_result",
    [
        ("john", "John"),
        ("123", AssertionError),
        ("", AssertionError),
        ("y2j", AssertionError),
    ],
)
def test_check_name(input_name, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_name(input_name)
    else:
        assert check_name(input_name) == expected_result


@pytest.mark.parametrize(
    "input_choice, expected_result",
    [
        ("r", "r"),
        ("R", "R"),
        ("z", AssertionError),
        ("rrx", AssertionError),
        ("1", AssertionError),
    ],
)
def test_check_scenario(input_choice, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_scenario(input_choice)
    else:
        assert check_scenario(input_choice) == expected_result


@pytest.mark.parametrize(
    "input_choice, expected_result",
    [
        ("s", "s"),
        ("D", "D"),
        ("z", AssertionError),
        ("rrx", AssertionError),
        ("1", AssertionError),
    ],
)
def test_check_project_choice(input_choice, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_project_choice(input_choice)
    else:
        assert check_project_choice(input_choice) == expected_result


@pytest.mark.parametrize(
    "input_choice, expected_result",
    [
        ("t", "t"),
        ("D", "D"),
        ("z", AssertionError),
        ("rrx", AssertionError),
        ("1", AssertionError),
    ],
)
def test_check_edit_project_choice(input_choice, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_edit_project_choice(input_choice)
    else:
        assert check_edit_project_choice(input_choice) == expected_result


@pytest.mark.parametrize(
    "input_email, expected_result",
    [
        ("test@example.com", "test@example.com"),
        ("Test243@exAmple.com.com", "test243@example.com.com"),
        ("invalid.email", AssertionError),
        ("@missingusername.com", AssertionError),
        ("no@dotcom", AssertionError),
        ("@.com", AssertionError),
        ("", AssertionError),
    ],
)
def test_check_email(input_email, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_email(input_email)
    else:
        assert check_email(input_email) == expected_result


@pytest.mark.parametrize(
    "input_choice, expected_result",
    [
        ("please", None),
        ("PLEASE", None),
        ("z", AssertionError),
        ("", AssertionError),
        ("1", AssertionError),
    ],
)
def test_check_activate_email(input_choice, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_activate_email(input_choice)
    else:
        assert check_activate_email(input_choice) == expected_result


@pytest.mark.parametrize(
    "input_password, input_confirm, expected_result",
    [
        ("password123", "password123", ("password123", "password123")),
        ("password", "confirm", AssertionError),
        ("", "password123", AssertionError),
        ("password123", "", AssertionError),
        ("", "", AssertionError),
    ],
)
def test_check_password(input_password, input_confirm, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_password(input_password, input_confirm)
    else:
        assert check_password(input_password, input_confirm) == expected_result


@pytest.mark.parametrize(
    "input_phone, expected_result",
    [
        ("01234567890", "01234567890"),
        ("1234567890", AssertionError),
        ("012345678901", AssertionError),
        ("abcdefghijk", AssertionError),
        ("", AssertionError),
    ],
)
def test_check_phone(input_phone, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_phone(input_phone)
    else:
        assert check_phone(input_phone) == expected_result


@pytest.mark.parametrize(
    "input_value, expected_result",
    [
        ("12345", "12345"),
        ("12.34", AssertionError),
        ("abc123", AssertionError),
        ("", AssertionError),
    ],
)
def test_check_number(input_value, expected_result):
    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_number(input_value)
    else:
        assert check_number(input_value) == expected_result


@pytest.fixture
def past_date():
    return (datetime.datetime.now() - datetime.timedelta(days=10)).strftime("%d/%m/%Y")


@pytest.fixture
def current_date():
    # Only can from next day
    return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")


@pytest.fixture
def future_date():
    return (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%d/%m/%Y")


@pytest.fixture
def assertion():
    return AssertionError


@pytest.fixture
def null_date():
    return None


@pytest.mark.parametrize(
    "_date, expected_result",
    [
        (
            "!#412",
            AssertionError,
        ),
        (
            "1df",
            AssertionError,
        ),
        (
            "dfasdf",
            AssertionError,
        ),
    ],
)
def test_check_date(_date, expected_result):
    with pytest.raises(expected_result):
        check_date(_date)


@pytest.mark.parametrize(
    "_date, expected_result",
    [
        (
            "current_date",
            "current_date",
        ),
        (
            "past_date",
            "assertion",
        ),
        (
            "future_date",
            "future_date",
        ),
    ],
)
def test_check_date_2(request, _date, expected_result):
    _date = request.getfixturevalue(_date)
    expected_result = request.getfixturevalue(expected_result)

    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_date(_date)
    else:
        assert check_date(_date) == _date


@pytest.mark.parametrize(
    "start_date, end_date, expected_result",
    [
        (
            "current_date",
            "future_date",
            "null_date",
        ),
        (
            "past_date",
            "future_date",
            "assertion",
        ),
        (
            "future_date",
            "future_date",
            "assertion",
        ),
    ],
)
def test_check_start_end_date(request, start_date, end_date, expected_result):
    start_date = request.getfixturevalue(start_date)
    end_date = request.getfixturevalue(end_date)
    expected_result = request.getfixturevalue(expected_result)

    if isinstance(expected_result, type):
        with pytest.raises(expected_result):
            check_start_end_date(start_date, end_date)
    else:
        assert check_start_end_date(start_date, end_date) == expected_result
