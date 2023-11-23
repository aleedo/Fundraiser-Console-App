import re


def check_scenario(s):
    assert re.match(r"^[rlx]$", s, re.I), "Sorry, Please choose one of `r`, `l`, `x`"
    return s
