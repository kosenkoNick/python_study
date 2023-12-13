from pytest import mark
from time_converter.converter__time_fromatting import time_converter as formatted_converter
from time_converter.converter__if_clause import time_converter as if_converter


@mark.parametrize('func', [formatted_converter, if_converter])
@mark.parametrize('time_in, time_expected', [("12:30 p.m.", "12:30"),
                                             ("9:00 a.m.", "09:00"),
                                             ("9:15 p.m.", "21:15"),
                                             ("11:15 p.m.", "23:15")])
def test__converter(func, time_in, time_expected):
    assert func(time_in) == time_expected
