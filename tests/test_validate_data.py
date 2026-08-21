import pytest
from source.validate_data import(
    validate_hour, 
    validate_season,
    validate_total_count,
    convert_row
)

def test_validate_hour():
    assert validate_hour(0) is True
    assert validate_hour(12) is True
    assert validate_hour(23) is True
    assert validate_hour(-1) is False
    assert validate_hour(24) is False

def test_validate_season():
    assert validate_season(1) is True
    assert validate_season(4) is True
    assert validate_season(0) is False
    assert validate_season(5) is False

def test_validate_total_count():
    assert validate_total_count(10, 20, 30) is True
    assert validate_total_count(10, 20, 25) is False

def test_convert_row():
    sample_row = {
        "instant": "1",
        "dteday": "2011-01-01",
        "season": "1",
        "yr": "0",
        "mnth": "1",
        "hr": "0",
        "holiday": "0",
        "weekday": "6",
        "workingday": "0",
        "weathersit": "1",
        "temp": "0.24",
        "atemp": "0.2879",
        "hum": "0.81",
        "windspeed": "0.0",
        "casual": "3",
        "registered": "13",
        "cnt": "16",
    }

    result = convert_row(sample_row)
    assert result["instant"]==1
    assert result["dteday"]=="2011-01-01"
    assert result["season"]==1
    assert result["temp"]==0.24
    assert result["casual"]==3
    assert result["cnt"]==16