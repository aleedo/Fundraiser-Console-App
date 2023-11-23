import re
from dateutil import parser
import datetime


def check_edit_project_choice(s):
    assert re.match(
        r"^[tdmse]$", s, re.I
    ), "Sorry, Please choose one of `t`, `d`, `m`, `s`, `e`"
    return s


def check_number(s):
    assert s.isdigit(), "Sorry not a valid Number"
    return s


def check_date(_date):
    date_parsed = None

    try:
        date_parsed = parser.parse(_date, dayfirst=True)
    except:
        raise AssertionError("Not a valid date.")

    assert date_parsed >= datetime.datetime.now(), f"Sorry date can't be in the past"
    return _date


def check_start_end_date(start_date, end_date):
    start_date_parsed = parser.parse(start_date, dayfirst=True)
    end_date_parsed = parser.parse(end_date, dayfirst=True)

    assert (
        start_date_parsed >= datetime.datetime.now()
    ), f"Sorry date can't be in the past"

    assert (
        start_date_parsed < end_date_parsed
    ), "Sorry date can't be after or the same as end date."
