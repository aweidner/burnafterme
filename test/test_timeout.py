from burnafterme.lib import parse_timeout


def test_parses_second_timeout():
    assert parse_timeout("1s") == 1    
    assert parse_timeout("300s") == 300


def test_parses_minute_timeout():
    assert parse_timeout("60s") == parse_timeout("1m")


def test_parses_hour_timeout():
    assert parse_timeout("1h") == parse_timeout("60m") 


def test_parses_day_timeout():
    assert parse_timeout("2d") == parse_timeout("48h") 


def test_parses_week_timeout():
    assert parse_timeout("2w") == parse_timeout("14d")


def test_parses_year_timeout():
    assert parse_timeout("365d") == parse_timeout("1y")
